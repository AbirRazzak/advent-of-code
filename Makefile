create-virtualenv:
	./scripts/create-virtualenv

clean-virtualenv:
	pyenv uninstall --force advent-of-code

update-deps:
	./scripts/update-deps
