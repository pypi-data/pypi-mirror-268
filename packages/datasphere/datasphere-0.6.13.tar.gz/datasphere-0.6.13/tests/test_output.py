from datasphere.api import jobs_pb2, project_pb2
from datetime import datetime, timezone
from google.protobuf.timestamp_pb2 import Timestamp

from datasphere.output import output, job_spec, project_spec, execution_data_spec, ExecutionData, Format


def test_jobs_table(tmp_path):
    jobs = [
        jobs_pb2.Job(
            id='bt12tlsc3nkt2opg2h61',
            name='my script',
            desc='This script is doing cool ML stuff',
            created_at=get_ts(datetime(year=2022, month=4, day=15, tzinfo=timezone.utc)),
            finished_at=get_ts(datetime(year=2022, month=4, day=16, tzinfo=timezone.utc)),
            status=jobs_pb2.JobStatus.SUCCESS,
            created_by_id='Bob',
        ),
        jobs_pb2.Job(
            id='bt10gr4c1b081bidoses',
            created_at=get_ts(datetime(year=2022, month=5, day=2, tzinfo=timezone.utc)),
            status=jobs_pb2.JobStatus.EXECUTING,
            created_by_id='Alice',
        )
    ]
    output_f = tmp_path / 'output'
    with open(output_f, 'w') as f:
        output(jobs, job_spec, f, Format.TABLE)
    assert output_f.read_text() == """
ID                    Name       Description                         Created at           Finished at          Status     Created by
--------------------  ---------  ----------------------------------  -------------------  -------------------  ---------  ------------
bt12tlsc3nkt2opg2h61  my script  This script is doing cool ML stuff  2022-04-15T00:00:00  2022-04-16T00:00:00  SUCCESS    Bob
bt10gr4c1b081bidoses                                                 2022-05-02T00:00:00                       EXECUTING  Alice
"""[1:]


def test_projects_json(tmp_path):
    projects = [
        project_pb2.Project(
            id='b3pps3ro4jq0ocj95kil',
            name='test project',
            community_id='b3p8be2lrvjd6sqkt42c',
        ),
        project_pb2.Project(
            id='b3pivi9ruk3cemjm74u6',
            community_id='b3p8be2lrvjd6sqkt42c',
        ),
    ]
    output_f = tmp_path / 'output'
    with open(output_f, 'w') as f:
        output(projects, project_spec, f, Format.JSON)
    assert output_f.read_text() == """
[
    {
        "id": "b3pps3ro4jq0ocj95kil",
        "name": "test project",
        "community_id": "b3p8be2lrvjd6sqkt42c"
    },
    {
        "id": "b3pivi9ruk3cemjm74u6",
        "name": "",
        "community_id": "b3p8be2lrvjd6sqkt42c"
    }
]
"""[1:]


def test_execution_data_json(tmp_path):
    execution_data = ExecutionData(job_id='b3pps3ro4jq0ocj95kil', operation_id='op')
    output_f = tmp_path / 'output'
    with open(output_f, 'w') as f:
        output([execution_data], execution_data_spec, f, Format.JSON)
    assert output_f.read_text() == """
{
    "job_id": "b3pps3ro4jq0ocj95kil",
    "operation_id": "op"
}
"""[1:]


def test_empty_data(tmp_path):
    output_table_f = tmp_path / 'output.table'
    with open(output_table_f, 'w') as f:
        output([], execution_data_spec, f, Format.TABLE)
    assert output_table_f.read_text() == """
Job ID    Operation ID
--------  --------------
"""[1:]

    output_json_f = tmp_path / 'output.json'
    with open(output_json_f, 'w') as f:
        output([], execution_data_spec, f, Format.JSON)
    assert output_json_f.read_text() == '[]\n'


def get_ts(dt: datetime) -> Timestamp:
    ts = Timestamp()
    ts.FromDatetime(dt)
    return ts
