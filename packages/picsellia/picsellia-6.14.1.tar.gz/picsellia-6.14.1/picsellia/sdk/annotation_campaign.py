import logging
import os
import warnings
from datetime import date
from typing import Dict, List, Optional, Tuple, Union
from uuid import UUID

from beartype import beartype
from beartype.roar import BeartypeDecorHintPep585DeprecationWarning
from orjson import orjson

from picsellia.colors import Colors
from picsellia.decorators import exception_handler
from picsellia.sdk.asset import Asset, MultiAsset
from picsellia.sdk.connexion import Connexion
from picsellia.sdk.dao import Dao
from picsellia.sdk.job import Job
from picsellia.sdk.taggable import Taggable
from picsellia.sdk.worker import Worker
from picsellia.types.enums import CampaignStepType, ObjectDataType
from picsellia.types.schemas import AnnotationCampaignSchema
from picsellia.utils import filter_payload

warnings.filterwarnings("ignore", category=BeartypeDecorHintPep585DeprecationWarning)
logger = logging.getLogger("picsellia")


class AnnotationCampaign(Dao, Taggable):
    def __init__(self, connexion: Connexion, data: dict):
        Dao.__init__(self, connexion, data)

    def __str__(self):
        return f"{Colors.GREEN}Annotation Campaign {self.name}{Colors.ENDC} for dataset version {self.dataset_version_id} (id: {self.id})"

    @property
    def dataset_version_id(self) -> UUID:
        """UUID of the (DatasetVersion) of this campaign"""
        return self._dataset_version_id

    @property
    def name(self) -> str:
        """Name of the campaign"""
        return self._name

    @exception_handler
    @beartype
    def refresh(self, data: dict):
        schema = AnnotationCampaignSchema(**data)
        self._name = schema.name
        self._dataset_version_id = schema.dataset_version_id
        return schema

    @exception_handler
    @beartype
    def sync(self) -> dict:
        r = self.connexion.get(f"/sdk/campaigns/annotation/{self.id}").json()
        self.refresh(r)
        return r

    @exception_handler
    @beartype
    def update(
        self,
        name: Optional[str] = None,
        description: Optional[str] = None,
        instructions_object_name: Optional[str] = None,
        instructions_text: Optional[str] = None,
        end_date: Optional[date] = None,
        auto_add_new_assets: Optional[bool] = None,
        auto_close_on_completion: Optional[bool] = None,
    ) -> None:
        """Update this campaign parameters

        Examples:
            ```python
            foo_campaign.update(name="another-name")
            ```

        Arguments:
            name (str, optional): name of the campaign. Defaults to None.
            description (str, optional): Description of the campaign. Defaults to None.
            instructions_object_name (str, optional): Instructions file object name stored on S3. Defaults to None.
            instructions_text (str, optional): Instructions text. Defaults to None.
            end_date (date, optional): End date of the campaign. Defaults to None.
            auto_add_new_assets (bool, optional):
                If true, new assets of this dataset will be added as a task in the campaign.  Defaults to None.
            auto_close_on_completion (bool, optional):
                If true, campaign will be close when all tasks will be done. Defaults to None.

        """
        payload = {
            "name": name,
            "description": description,
            "instructions_object_name": instructions_object_name,
            "instructions_text": instructions_text,
            "end_date": end_date,
            "auto_add_new_assets": auto_add_new_assets,
            "auto_close_on_completion": auto_close_on_completion,
        }
        filtered_payload = filter_payload(payload)
        r = self.connexion.patch(
            f"/sdk/campaigns/annotation/{self.id}", data=orjson.dumps(filtered_payload)
        ).json()
        self.refresh(r)
        logger.info(f"{self} updated")

    @exception_handler
    @beartype
    def upload_instructions_file(self, path: str) -> None:
        """Upload instructions for this campaign

        Examples:
            ```python
            foo_campaign.upload_instructions_file("/path/to/file.pdf")
            ```

        Arguments:
            path (str): Path of instructions file

        """
        instruction_file_name = os.path.basename(path)
        object_name = self.connexion.generate_dataset_version_object_name(
            instruction_file_name,
            ObjectDataType.CAMPAIGN_FILE,
            dataset_version_id=self.dataset_version_id,
        )
        self.connexion.upload_file(object_name, path)
        self.update(instructions_object_name=object_name)

    @exception_handler
    @beartype
    def delete(self) -> None:
        """Delete a campaign.

        :warning: **DANGER ZONE**: Be very careful here!

        It will remove this campaign from our database, all tasks and assignments will be removed.
        This will not delete annotations and assets.

        Examples:
            ```python
            foo_campaign.delete()
            ```
        """
        self.connexion.delete(f"/sdk/campaigns/annotation/{self.id}")
        logger.info(f"{self} deleted")

    @exception_handler
    @beartype
    def add_step(
        self,
        name: str,
        type: Union[CampaignStepType, str],
        description: Optional[str] = None,
        assignees: Optional[List[Tuple[Union[Worker, UUID], Union[float, int]]]] = None,
        order: Optional[int] = None,
    ) -> dict:
        """Add a step on this campaign.

        Examples:
            ```python
            workers = foo_dataset.list_workers()
            # In first step, 2 over 3 annotation task will be assigned to worker 1, third one is going to worker 0
            foo_campaign.add_step(
                name="annotation-step",
                type="ANNOTATION",
                description="annotation step",
                assignees=[(workers[0], 1.0), (workers[1], 2.0)]
            )
            # In second step, all review task will be assigned to worker 2
            foo_campaign.add_step(
                name="review-step",
                type="REVIEW",
                description="review step",
                assignees=[(workers[2], 1)]
            )
            ```
        Arguments:
            name (str): name of the step
            type (str or CampaignStepType): Type of the step: can be ANNOTATION or REVIEW
            description (str, optional): Description of the step. Defaults to None.
            assignees (list of tuple of (worker or UUID), float, optional): Can be used to assign workers to this step.
                Defaults to None.
            order (int, optional): Index where to insert the step in the workflow, the step will be appended at the end
                if nothing is specified. Defaults to None.

        Returns:
            dict, data of this step
        """
        campaign_step_type = CampaignStepType.validate(type)
        payload = {
            "name": name,
            "type": campaign_step_type,
            "description": description,
            "order": order,
        }
        if assignees:
            payload["assignees"] = [
                {
                    "worker_id": worker.id if isinstance(worker, Worker) else worker,
                    "weight": weight,
                }
                for worker, weight in assignees
            ]

        r = self.connexion.post(
            f"/sdk/campaigns/annotation/{self.id}/steps",
            data=orjson.dumps(payload),
        ).json()
        logger.info(f"Step {name} has been added to campaign {self.name}")
        return r

    @exception_handler
    @beartype
    def list_steps(self) -> List[Dict]:
        """List all the steps of this campaign.

        Returns:
            a list of steps of this campaign as python dict
        """
        r = self.connexion.get(f"/sdk/campaigns/annotation/{self.id}/steps").json()
        return r["items"]

    @exception_handler
    @beartype
    def launch(
        self, existing_annotations_step_id: Union[str, UUID, None] = None
    ) -> Job:
        """Launch this campaign, creating assignments on steps you have created before.

        Examples:
            ```python
            workers = foo_dataset.list_workers()
            foo_campaign = foo_dataset_version.create_campaign("foo-campaign")
            foo_campaign.add_step(
                name="annotation-step",
                type="ANNOTATION",
                assignees=[(workers[0], 1.0), (workers[1], 2.0)]
            )
            review_step = foo_campaign.add_step(
                name="review-step",
                type="REVIEW",
                assignees=[(workers[2], 1)]
            )
            foo_campaign.launch(existing_annotations_step_id=review_step["id"])
            ```

        Arguments:
            existing_annotations_step_id (UUID or str, optional):
                If given, will create assignments for existing annotations on given step_id.
                You also can give "DONE" in this field, it will create assignments in DONE last step. Defaults to None.

        Returns:
            a Job, that you can wait for.
        """
        return self._create_assignments(
            existing_annotations_step_id=existing_annotations_step_id
        )

    @exception_handler
    @beartype
    def _create_assignments(
        self,
        assets: Union[List[Asset], MultiAsset, None] = None,
        workers: Optional[List[Union[Worker, UUID]]] = None,
        existing_annotations_step_id: Union[str, UUID, None] = None,
    ) -> Job:
        """Create assignments for this campaign.

        Arguments:
            assets (list of (Asset) or (MultiAsset), optional):
                if given, will only create assignments on these assets. Defaults to None
            workers (list of (Worker) or worker id, optional):
                if given, will only create assignments for these workers. Defaults to None
            existing_annotations_step_id (UUID or str, optional):
                If given, will create assignments for existing annotations on given step_id.
                You also can give "DONE" in this field, it will create assignments in DONE last step. Defaults to None.

        Returns:
            a Job, that you can wait for.
        """
        payload = {}
        if assets:
            payload["asset_ids"] = [asset.id for asset in assets]
        if workers:
            payload["worker_ids"] = [
                worker.id if isinstance(worker, Worker) else worker
                for worker in workers
            ]
        if existing_annotations_step_id:
            payload["existing_annotations_step_id"] = existing_annotations_step_id
        r = self.connexion.post(
            f"/sdk/campaigns/annotation/{self.id}/assignments/bulk/job",
            data=orjson.dumps(payload),
        ).json()
        self.refresh(r["campaign"])
        return Job(self.connexion, r["job"], version=2)
