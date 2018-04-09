
PROJECT = wonderful-datastore-getbykey
VIRTUAL_ENV = venv
FUNCTION_NAME = wonderful-datastore-getbykey
AWS_REGION = us-east-1
FUNCTION_HANDLER = lambda_handler
LAMBDA_ROLE = arn:aws:iam::1234567890:role/my-execution-role

# Default commands
install: virtual
build: clean_package build_package_tmp copy_python remove_unused zip

virtual:
	@echo "--> Setup and activate virtualenv"
	if test ! -d "$(VIRTUAL_ENV)"; then \
	    pip install virtualenv; \
	    virtualenv $(VIRTUAL_ENV);\
	    source venv/bin/activate;\
	    pip install -r requirements.txt; \
	fi
	@echo ""

clean_package:
	rm -rf ./package/*

build_package_tmp:
	@echo ""
	mkdir -p ./package/tmp/lib
	cp -a ./$(PROJECT)/. ./package/tmp
	@echo ""

copy_python:
	if test -d $(VIRTUAL_ENV)/lib; then \
	    cp -a ./$(VIRTUAL_ENV)/lib/python3.5/site-packages/. ./package/tmp; \
	    cp -a /usr/local/lib/python3.5/dist-packages/pymysql/ ./package/tmp;\
	fi
	if test -d $(VIRTUAL_ENV)/lib64; then \
	    cp -a ./$(VIRTUAL_ENV)/lib64/python3.5/site-packages/. ./package/tmp; \
	fi

remove_unused:
	rm -rf ./package/tmp/wheel*
	rm -rf ./package/tmp/easy-install*
	rm -rf ./package/tmp/setuptools*

zip:
	cd ./package/tmp && zip -r ../$(PROJECT).zip .