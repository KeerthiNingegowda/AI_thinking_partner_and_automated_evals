import duckdb

path = "/Users/keerthiningegowda/Desktop/skill_eval/AI_thinking_partner_and_automated_evals/kt.jsonl"
con = duckdb.connect()
con.sql(f"""
create or replace view raw as
select filename, row_number() over () as line, json as j
from read_json_objects('{path}', format='newline_delimited', ignore_errors=true, filename=true)
""")
print(con.sql("select j->>'type' as type, count(*) as n from raw group by 1 order by n desc"))