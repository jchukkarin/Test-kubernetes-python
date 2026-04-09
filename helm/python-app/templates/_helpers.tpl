{{- define "python-app.name" -}}
python-app
{{- end }}

{{- define "python-app.fullname" -}}
{{ .Release.Name }}-python-app
{{- end }}

{{- define "python-app.serviceAccountName" -}}
default
{{- end }}