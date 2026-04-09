{{- define "project-app.name" -}}
project-app
{{- end }}

{{- define "project-app.fullname" -}}
{{ .Release.Name }}-project-app
{{- end }}

{{- define "project-app.serviceAccountName" -}}
default
{{- end }}