from source import repo_checker
from source import SMTP
from source import logger
import time


def daemon_loop(config):
    while True:
        repo_result = repo_checker.main(config)
        log = logger.ingestor(repo_result, config['log_file_location'])
        SMTP.main(config['smtp_config'], str.join('\n', log))


def failable(function):
    try:
        function
    except BaseException as e:
        time.sleep(60)
        function
        print(e)


if __name__ == '__main__':
    failable(daemon_loop(repo_checker.load_from_json('daemon.config')))
