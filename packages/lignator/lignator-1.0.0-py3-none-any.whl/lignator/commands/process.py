import uuid
import pathlib
import json
import inflection
from datetime import datetime

import lignator as lg
from lignator import logger


def process(dt, *, start_time, end_time):
    process_uuid = uuid.uuid4()

    result = {
        'id': process_uuid,
    }

    metrics_count = len(dt.metrics)
    logger.info(f"Son {metrics_count} métricas")

    metrics_list = dt.metrics
    result['metrics'] = metrics_list

    today = datetime.today()
    basedir = '/tmp/lignator'

    output_dir = f"{basedir}/processed/{today.year}/{today.month:02d}/{today.day:02d}/{process_uuid}"
    pathlib.Path(output_dir).mkdir(parents=True, exist_ok=True)
    result['dir'] = output_dir

    result['data'] = {}
    for metric in metrics_list:
        logger.info(f"procesando métrica: {metric}")

        name = metric['name']
        unit = metric['unit']
        proc = metric['proc']

        metric_data = dt.metric_data(name, unit, proc)

        if start_time:
            metric_data = metric_data[metric_data['timestamp'] >= start_time]

        if end_time:
            metric_data = metric_data[metric_data['timestamp'] < end_time]

        rows_count = metric_data.shape[0]
        if rows_count > 0:
            result['data'][name] = {
                'name': name,
                'unit': unit,
                'proc': proc,
                'first_time': metric_data['timestamp'].min(),
                'last_time': metric_data['timestamp'].max(),
            }

            filename = inflection.parameterize(name)
            output_path = f"{output_dir}/{filename}.csv.gz"
            metric_data.to_csv(output_path, index=False, compression='gzip')

            result['data'][name]['path'] = output_path

            logger.info(f"escribiendo: {output_path}")

        else:
            logger.info(f"No hay datos nuevos: {metric}")


    json_data = json.dumps(result, default=str)
    with open(f"{output_dir}/result.json", "w") as out:
        out.write(json_data)

    return result
