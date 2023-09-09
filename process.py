import apache_beam as beam
from apache_beam.io import ReadFromText
from apache_beam.options.pipeline_options import PipelineOptions


from utils.csv_utils import parse_csv
from transformators.basic_transformator import dummy_transformator
from validators.basic_validators import dummy_validator
from mappings.schemas import PG_SCHEMAS


options = PipelineOptions()
options.view_as(
    beam.options.pipeline_options.SetupOptions).save_main_session = True


with beam.Pipeline(options=options) as p:
    data = (
        p
        | "Read CSV" >> ReadFromText("partners_data.csv")
        | "Parse CSV" >> beam.Map(parse_csv)
        | "Validate Data" >> beam.Map(dummy_validator)
        | "Transform Data" >> beam.Map(dummy_transformator)
    )

    # Once we have the GCP configured we can store this into a DB

    # data | "Write to PostgreSQL" >> beam.io.WriteToBigQuery(
    #     table="your_project_id.your_dataset_id.your_table_id",
    #     schema=PG_SCHEMAS["partners_data"],
    #     create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
    #     write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND,
    # )
