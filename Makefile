
.PHONY: clean

clean:
	-rm -rf build/ *.egg-info/ temp/ MANIFEST dist/ saga/VERSION pylint.out *.egg
	make -C docs clean
	find . -name \*.pyc -exec rm -f {} \;

