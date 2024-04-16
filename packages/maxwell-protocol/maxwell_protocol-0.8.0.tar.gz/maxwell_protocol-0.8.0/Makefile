prj-dir := $(shell pwd)
src-dir := $(prj-dir)
venv-dir := $(prj-dir)/venv
python-native := python3
python := $(venv-dir)/bin/python
pytest := $(venv-dir)/bin/pytest
pip := $(venv-dir)/bin/pip
pip-compile := $(venv-dir)/bin/pip-compile

define get_site_dir
$(shell $(python) -c "import sysconfig; print(sysconfig.get_path(\"purelib\"))")
endef

init: create-env install-build-tools install-deps set-path gen

create-env:
	$(python-native) -m venv $(venv-dir)

install-build-tools:
	$(pip) install --upgrade pip
	$(pip) install pip-tools

install-deps:
	$(pip-compile) --strip-extras
	$(pip) install -r requirements.txt

install-optional-deps:
	$(pip) install .[test]

set-path:
	echo $(src-dir) > $(call get_site_dir)/my.pth

run:
	$(python) $(filter-out $@, $(MAKECMDGOALS))

test:
	$(pytest)

gen:
	$(prj-dir)/bin/gen_protocol_code.sh

publish:
	$(python) -m build && twine check dist/* && twine upload -r pypi dist/*

publish-test:
	$(python) -m build && twine check dist/* && twine upload -r pypitest dist/*

clean:
	$(prj-dir)/bin/clean_protocol_code.sh
	rm -rf $(venv-dir) $(prj-dir)/build $(prj-dir)/dist ${prj-dir}/maxwell_protocol.egg-info
