
default: readme license

readme:
	@echo "Recompiling README ..."
	readmix --compile --markdown README.rx
	@echo "    Done."

license:
	@echo "Recompiling LICENSE ..."
	readmix --compile --markdown LICENSE.rx
	@echo "    Done."

publish:
	@echo "Publishing to NPM ..."
	@npm publish
	@echo "    Done."
