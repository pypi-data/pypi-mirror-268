import argparse
import logging
from logging.handlers import RotatingFileHandler
from pan_ztp_patcher.ztp_patcher import (
    get_api_key,
    scp_import_content,
    send_api_request,
    job_monitor,
)


def main():
    # Configure logging
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Configure file handler for debug level
    file_handler = RotatingFileHandler(
        "debug.log", maxBytes=5 * 1024 * 1024, backupCount=10
    )
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )  # noqa E501
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    # Configure console handler for info level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter("%(message)s")
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description="Update content version on PAN-OS firewalls",
    )
    parser.add_argument(
        "--pi-hostname",
        required=True,
        help="Raspberry Pi hostname or IP address",
    )
    parser.add_argument(
        "--pi-username",
        required=True,
        help="Raspberry Pi username",
    )
    parser.add_argument(
        "--pi-password",
        required=True,
        help="Raspberry Pi password",
    )
    parser.add_argument(
        "--pan-hostname",
        required=True,
        help="PAN-OS firewall hostname or IP address",
    )
    parser.add_argument(
        "--pan-username",
        required=True,
        help="PAN-OS firewall username",
    )
    parser.add_argument(
        "--pan-password",
        required=True,
        help="PAN-OS firewall password",
    )
    parser.add_argument(
        "--content-path",
        default="/var/tmp/",
        help="Content path on the Raspberry Pi (default: /var/tmp/)",
    )
    parser.add_argument(
        "--content-file",
        default="panupv2-all-contents-8834-8684",
        help="Content file name (default: panupv2-all-contents-8834-8684)",
    )
    args = parser.parse_args()

    # Firewall connection details
    pan_hostname = args.pan_hostname
    pan_username = args.pan_username
    pan_password = args.pan_password

    # Raspberry Pi connection details
    pi_hostname = args.pi_hostname
    pi_username = args.pi_username
    pi_password = args.pi_password
    content_path = args.content_path
    content_file = args.content_file

    # Call the functions
    api_key = get_api_key(
        pan_hostname,
        pan_username,
        pan_password,
    )
    if api_key:
        logger.info("API Key: {}".format(api_key))
    else:
        logger.error("Failed to retrieve the API key.")
        return

    scp_import_content(
        pan_hostname,
        pan_username,
        pan_password,
        pi_hostname,
        pi_username,
        pi_password,
        content_path,
        content_file,
    )
    job_id = send_api_request(
        pan_hostname,
        api_key,
        content_file,
    )
    if job_id:
        job_monitor(
            pan_hostname,
            api_key,
            job_id,
        )
    else:
        logger.error("Failed to retrieve the job ID.")


if __name__ == "__main__":
    main()
