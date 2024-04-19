from functools import cached_property

import boto3

from reach_commons.app_logging.logger import get_reach_logger


class S3Client:
    def __init__(
        self,
        logger=get_reach_logger(),
        region_name="us-east-1",
        profile_name=None,
    ):
        self.logger = logger
        self.region_name = region_name
        self.profile_name = profile_name

    @cached_property
    def client(self):
        session = boto3.Session(
            region_name=self.region_name, profile_name=self.profile_name
        )

        return session.client("s3")

    def get_object(self, s3_bucket_name, s3_key):
        try:
            s3_object = self.client.get_object(Bucket=s3_bucket_name, Key=s3_key)
            actual_message_body = s3_object["Body"].read().decode("utf-8")

            self.logger.info(
                f"Retrieved object from S3: {s3_key} from bucket: {s3_bucket_name}"
            )
            return actual_message_body
        except Exception as e:
            self.logger.error(
                f"Error retrieving object {s3_key} from bucket: {s3_bucket_name}: {str(e)}"
            )

        return None
