### Django FHIR Server

This is an open-source Django FHIR Server that can be used as a starting point for any python based back-end project. This server provides basic FHIR validation and APIs that can be extended in any required manner.

This project is powered by:

- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)

## Development Status

We're working on adding new resources as soon as possible. Below are the resources that have already been added and are fully supported by this FHIR server.

### Active FHIR Resources

#### Foundation

| Conformance | Terminology | Security | Documents | Other |
| ----------- | ----------- | -------- | --------- | ----- |
| -           | -           | -        | -         | -     |

#### Base

| Individuals                                 | Entities #1 | Entities #2 | Workflow | Management |
| ------------------------------------------- | ----------- | ----------- | -------- | ---------- |
| [Patient](http://hl7.org/fhir/patient.html) | -           | -           | -        | -          |

#### Clinical

| Summary | Diagnostics | Medications | Care Provision | Request & Response |
| ------- | ----------- | ----------- | -------------- | ------------------ |
| -       | -           | -           | -              | -                  |

#### Financial

| Support | Billing | Payment | General |
| ------- | ------- | ------- | ------- |
| -       | -       | -       | -       |

#### Specialized

| Public Health & Research | Definitional Artifacts | Evidence-Based Medicine | Quality Reporting & Testing | Medication Definition |
| ------------------------ | ---------------------- | ----------------------- | --------------------------- | --------------------- |
| -                        | -                      | -                       | -                           | -                     |

### Todo Items

- Docker Compose
- Support RDBMS
- Support MongoDB
