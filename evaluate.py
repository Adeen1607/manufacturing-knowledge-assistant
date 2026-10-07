"""Small developer-authored fixture evaluation, not a held-out production benchmark."""
import json
from collections import Counter
from core import ROOT, answer_question

def evaluate():
    cases=json.loads((ROOT/'data/evaluation.json').read_text()); results=[]
    for case in cases:
        actual=answer_question(case['question'],case['role'])
        source_ok=not case.get('source') or bool(actual['sources'] and actual['sources'][0]['id']==case['source'])
        results.append({**case,'actual_status':actual['status'],'source_ids':[s['id'] for s in actual['sources']],
                        'passed':actual['status']==case['status'] and source_ok})
    answerable=[r for r in results if r.get('source')]
    report={'mode':'offline extractive; LLM generation not evaluated','dataset':'30 developer-authored synthetic fixtures; not held out',
            'cases':len(results),'passed':sum(r['passed'] for r in results),
            'status_accuracy':sum(r['actual_status']==r['status'] for r in results)/len(results),
            'expected_source_hit_at_1':sum(bool(r['source_ids'] and r['source_ids'][0]==r['source']) for r in answerable)/len(answerable),
            'expected_status_counts':dict(Counter(r['status'] for r in results)),
            'results':results}
    (ROOT/'reports').mkdir(exist_ok=True); (ROOT/'reports/evaluation-results.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='results'},indent=2))
    print('Failures:',json.dumps([r for r in results if not r['passed']],indent=2))
    return report
if __name__=='__main__': evaluate()
