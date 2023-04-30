pre-commit install --allow-missing-config
pre-commit install --hook-type commit-msg --allow-missing-config
cp -rf scripts/local_pre-commit/post-commit .git/hooks/post-commit
chmod ug+x .git/hooks/*