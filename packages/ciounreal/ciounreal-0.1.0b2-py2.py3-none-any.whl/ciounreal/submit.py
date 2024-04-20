import json

import re

from ciocore import conductor_submit


def main(*args):
    (payload,) = args
    print("Conductor::submit::main() - Got Payload")
    submission_data = json.loads(payload)
    print("Conductor::submit::main() - Created Submission Data")
    
    try:
        print("Conductor::submit::main() - Trying to Submit Job")
        remote_job = conductor_submit.Submit(submission_data)
        print("Conductor::submit::main() - Submitted Job")
        response, response_code = remote_job.main()
        print("Conductor::submit::main() - Got Response")
        return json.dumps({"code": response_code, "response": response}, indent=4)
    except BaseException as ex:
        print("Conductor::submit::main() - Exception occurred while submitting job.")
        return json.dumps({"code": "undefined", "response": ex}, indent=4)


def test_cmd(*args):
    (payload,) = args
    submission_data = json.loads(payload)
    print("Conductor::submit::test_cmd - Got Payload")
    tasks = submission_data["tasks_data"]
    print("Conductor::submit::test_cmd - Got Tasks")
    sample = int(len(tasks) / 2)
    print("Conductor::submit::test_cmd - Returning Sample Task")
    return tasks[sample]["command"]
