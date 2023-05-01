
default: license

license:
	@echo "Recompiling LICENSE ..."
	readmix --compile --markdown LICENSE.rx
	@echo "    Done."

publish:
	@echo "Publishing to NPM ..."
	@npm publish
	@echo "    Done."
