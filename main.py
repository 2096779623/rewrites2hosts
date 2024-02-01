import yaml,sys
print("\n".join([f"{rewrite['domain']} {rewrite['answer']}" for rewrite in yaml.load(open(sys.argv[1], 'r', encoding='utf-8').read(), Loader=yaml.FullLoader)['filtering']['rewrites']]))
