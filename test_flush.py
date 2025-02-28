from time import sleep

for i in range(10):
    print(
        f"\r{i}--\b{i+1} {i+2}",
        end="",
        flush=True
    )
    sleep(0.5)
print(f"\r     \r", end="")


pattern = r"\w*rupture\w*membrane\w*"
strings = [
    "prematurerupturedmembranes",
    "primarycs39wks",
    "prolongedruptureofmembranes",
    "repeat",
    "repeatat38weeksforiugr",
    "repeatcsession",
    "rightlegpainfluidcheck",
    "ruptureofmembranes",
]

for s in strings:
    match = re.match(pattern, s)
    if match:
        print(f"Matched: {match.group()}")
    else:
        print(f"No match found in string: {s}")


bh_list = ['99acd',
'abnormalbehavior',
'acuteexacerbationofchronicparanoidschizophrenia',
'acutepsychosis',
'acutesycosis',
'agressiveschizophreniaf29',
'auditoryhallucinationspara',
'bh',
'bhdisastertransfer',
'bipolar',
'bipolardepression',
'bipolardisorder',
'ce',
'complaintnotgiven',
'confuseddisorganized',
'depression',
'depressionschizoaffectivedo',
'depressionsi',
'depressionwithpsyc',
'depressionwithsi',
'depressionwithsuic',
'depressionwithsuicidalideation',
'depressionwithsuicidalideations',
'depressionwithsuicidalideationsandattempt',
'depressionwthsuicialideation',
'depressivedo',
'disruptivemooddysregulationdisorder',
'dmdd',
'dxalcoholntoxication',
'eatingdisordermajordepressivedisorder',
'ereval',
'homicidalideation',
'intentionaloverdoseoftrazodonecmshcc',
'majordepression',
'majordepressionsuicidalideation',
'majordepressionsuicidalthoughts',
'majordepressionwithpsychosis',
'majordepressivedisorder',
'majordepressivedisorderrecurent',
'majordepressivedo',
'majordispressiondisorder',
'mdd',
'mddalcoholusedisorder',
'mddrecurrentsevere',
'mddwithpsychosis',
'medicalclearance',
'medicalclearancesuicidalattemps',
'mentalhealth',
'mentalhealthproblem',
'metalevaluation',
'mooddisorder',
'nocomplaintgiven',
'odd',
'overdose',
'paranoidschizophrenia',
'paranoidschizophreniaba',
'psycheval',
'psychosis',
'psychosisnos',
'psychosisunspecifiedtype',
'psychoticdisorder',
'psychproblem',
'ptsd',
'rash',
'schizoaffective',
'schizoaffectivedepressivetype',
'schizoaffectivedisorderdepressivetype',
'schizoaffectivedo',
'schizoaffectivedooverdosedepression',
'schizophrenia',
'schizophreniabipolar',
'schizophreniainacuteexacerbation',
'schizophreniaparanoidtype',
'schizophreniasuicidalideation',
'si',
'suicidal',
'suicidalideation',
'suicidalideations',
'suicideattempt',
'unknown',
'unspecifiedmooddisorder',
'unspecifiedpsychosis',
'unspeecifieddepressivedisorder',
]

bh_regex_list = [
    r"\w*depressi\w*",
    r"\w*schizo(?:phrenia|affective)?\w*",
    r"\w*suicid(?:al)?\w*",
    r"\w*psych(?:osis)?\w*",
    r"\w*mood\w*disorder\w*",
    r"\w*bipolar\w*",
    r"\w*mentalhealth\w*",
    r"\w*mdd\w*",
    "99acd",
    "abnormalbehavior",
    "acutesycosis",
    "auditoryhallucinationspara",
    "bh",
    "bhdisastertransfer",
    "ce",
    "complaintnotgiven",
    "confuseddisorganized",
    "dxalcoholntoxication",
    "ereval",
    "homicidalideation",
    "intentionaloverdoseoftrazodonecmshcc",
    "majordispressiondisorder",
    "medicalclearance",
    "metalevaluation",
    "nocomplaintgiven",
    "odd",
    "overdose",
    "ptsd",
    "rash",
    "si",
    "unknown",
]

from time import perf_counter

start_time = perf_counter()
for i in range(100):
    unmatched_strings = []
    for s in bh_list:
        matched = re.search('|'.join(bh_regex_list), s)
        if not matched:
            unmatched_strings.append(s)
end_time = perf_counter()
print(end_time - start_time)

start_time = perf_counter()
for i in range(100):
    unmatched_strings = []
    for s in ob_list:
        matched = False
        for r in regex_list:
            if re.search(r, s):
                matched = True
                break
        if not matched:
            unmatched_strings.append(s)
end_time = perf_counter()
print(end_time - start_time)



print(unmatched_strings)

with mlflow.start_run(run_name="model1") as run:
    mlflow.log_param("label", "price")
    mlflow.log_param("feature", "bedroom")
    mlflow.spark.log_model("model_name", "model", input_example=train_df.limit(5).toPandas())
    mlflow.log_metric("rmse", rmse)

from mlflow.tracking import MlflowClient
client = MlflowClient()
client.list_experiments()

experiment_id = run.info.experiment_id
run_df = mlflow.search_runs(experiment_id)


run_df = mlflow.search_runs(experiment_id, order_by=["msr"])

