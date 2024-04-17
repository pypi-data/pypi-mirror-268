#!/bin/bash
rm -rf /home/melodyecho/projects/Python/git-proj/melobot-docs/*
cp -r /home/melodyecho/projects/Python/git-proj/melobot/docs/build/html/* /home/melodyecho/projects/Python/git-proj/melobot-docs/
cp -r /home/melodyecho/projects/Python/git-proj/melobot/tests/private/pages/* /home/melodyecho/projects/Python/git-proj/melobot-docs/
cp /home/melodyecho/projects/Python/git-proj/melobot/tests/private/pages/.nojekyll /home/melodyecho/projects/Python/git-proj/melobot-docs/
