import os 
# os.system(f"npm install hexo-renderer-pug hexo-renderer-stylus --save&&npm install&&npm install hexo-deployer-git --save&&npm install hexo-generator-search --save&&npm install hexo-wordcount --save")
os.system(f"hexo clean&&hexo generate&&hexo server")
