local-build:
	docker-compose -f docker-compose.yml build

local-up:
	docker-compose -f docker-compose.yml up -d

local-rebuild:
	docker-compose -f docker-compose.yml up -d --build

local-backend-logs:
	docker-compose -f docker-compose.yml logs -f backend

local-test:
	pytest