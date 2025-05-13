dev:
	./scripts/dev.sh

build:
	./scripts/build_frontend.sh
	./scripts/build.sh

publish:
	uv publish