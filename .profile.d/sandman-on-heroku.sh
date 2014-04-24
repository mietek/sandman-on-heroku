#!/usr/bin/bash -e

if [ -z "${HEROKU_API_KEY}" ]; then
  echo "ERROR: HEROKU_API_KEY is not set"
  exit 1
fi

if [ -z "${DATABASE_OWNER_APP}" ]; then
  echo "ERROR: DATABASE_OWNER_APP is not set"
  exit 1
fi

CONFIG_VARS_URL="https://api.heroku.com/apps/${DATABASE_OWNER_APP}/config-vars"
HEROKU_AUTH=`echo -n :${HEROKU_API_KEY} | base64`

export DATABASE_URL=`curl -sfS "${CONFIG_VARS_URL}" \
		-H "Accept: application/vnd.heroku+json; version=3" \
		-H "Authorization: ${HEROKU_AUTH}" \
  | grep DATABASE_URL \
	| cut -d '"' -f 4`

# TODO: Remove when https://github.com/jeffknupp/sandman/pull/75 is merged
cat << EOF | patch -u /app/.heroku/python/lib/python2.7/site-packages/sandman/decorators.py
--- decorators.py
+++ decorators.py
@@ -40,3 +40,15 @@
                 rv = not_modified()
         return rv
     return wrapped
+
+
+def not_modified():
+    response = jsonify({'status': 304, 'error': 'not modified'})
+    response.status_code = 304
+    return response
+
+
+def precondition_failed():
+    response = jsonify({'status': 412, 'error': 'precondition failed'})
+    response.status_code = 412
+    return response
EOF
