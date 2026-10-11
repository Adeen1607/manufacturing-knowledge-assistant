from pathlib import Path
import json
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'reports/figures';OUT.mkdir(parents=True,exist_ok=True)
data=json.loads((ROOT/'reports/evaluation-results.json').read_text())
fig,ax=plt.subplots(figsize=(7,4));ax.bar(['Passed','Failed'],[data['passed'],data['cases']-data['passed']],color=['#2563eb','#b45309']);ax.set(title='Offline synthetic fixture outcomes',ylabel='Fixture count');fig.tight_layout();fig.savefig(OUT/'fixture-outcomes.png',dpi=160);plt.close(fig)
