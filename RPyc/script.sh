dockebuild . --tag rewreu/rypc


docker run -it --rm -p 18812:18812 rewreu/rypc python usr/local/bin/rpyc_classic.py --host 0.0.0.0