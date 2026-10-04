import yaml,glob,os
here=os.path.dirname(os.path.abspath(__file__))+'/..'
for f in sorted(glob.glob(here+'/genres/*.yaml')):
    g=yaml.safe_load(open(f))
    if len(g['cards'])>=10: print(g['id'],len(g['cards']))
