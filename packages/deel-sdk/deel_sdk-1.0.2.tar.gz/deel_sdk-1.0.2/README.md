# DeelSdk Python SDK 1.0.2

A Python SDK for DeelSdk.

- API version: 1.25.0
- SDK version: 1.0.2

Deel REST API

## Table of Contents

- [Installation](#installation)
- [Authentication](#authentication)
- [Environments](#environments)
- [Using Union Types in Function Parameters](#using-union-types-in-function-parameters)
- [Services](#services)

## Installation

```bash
pip install deel-sdk
```

## Authentication

### Access Token

The DeelSdk API uses a access token as a form of authentication.

The access token can be set when initializing the SDK like this:

```py
DeelSdk(
    access_token="YOUR_ACCESS_TOKEN"
)
```

Or at a later stage:

```py
sdk.set_access_token("YOUR_ACCESS_TOKEN")
```

## Environments

Here is the list of all available environment variables:

```py
Demo = "https://api-staging.letsdeel.com/rest/v2"
Production = "https://api.letsdeel.com/rest/v2"
```

Here is how you set an environment:

```py
from deel_sdk import Environment

sdk.set_base_url(Environment.Demo.value)
```

## Using Union Types in Function Parameters

In Python, a parameter can be annotated with a Union type, indicating it can accept values of multiple types.

### Passing Instances or Dictionaries

When we have a model such as:

```py
ParamType = Union[TypeA, TypeB]
```

utilized in a service as follows

```py
def service_method(param: ParamType):
    # Function implementation
```

You can call `service_method` with an instance of `TypeA`, `TypeB`, or a dictionary that can be converted to an instance of either type.

```python
type_a = TypeA(key="value")
type_b = TypeB(key="value")

sdk.service.service_method(type_a)
sdk.service.service_method(type_b)
sdk.service.service_method({"key": "value"})
```

### Note on Union Instances

You cannot create an instance of a Union type itself. Instead, pass an instance of one of the types in the Union, or a dictionary that can be converted to one of those types.

## Services

A list of all SDK services. Click on the service name to access its corresponding service methods.

| Service                                             |
| :-------------------------------------------------- |
| [AccountingService](#accountingservice)             |
| [ManagersService](#managersservice)                 |
| [PeopleService](#peopleservice)                     |
| [EorService](#eorservice)                           |
| [GlobalPayrollService](#globalpayrollservice)       |
| [ContractorsService](#contractorsservice)           |
| [AdjustmentsService](#adjustmentsservice)           |
| [CandidatesService](#candidatesservice)             |
| [PartnerManagedService](#partnermanagedservice)     |
| [ContractsService](#contractsservice)               |
| [TasksService](#tasksservice)                       |
| [TimesheetsService](#timesheetsservice)             |
| [MilestonesService](#milestonesservice)             |
| [OffCyclePaymentsService](#offcyclepaymentsservice) |
| [TimeOffService](#timeoffservice)                   |
| [InvoicesService](#invoicesservice)                 |
| [OrganizationsService](#organizationsservice)       |
| [LookupsService](#lookupsservice)                   |
| [WebhooksService](#webhooksservice)                 |
| [TokenService](#tokenservice)                       |
| [CartaService](#cartaservice)                       |

### AccountingService

A list of all methods in the `AccountingService` service. Click on the method name to view detailed information about that method.

| Methods                                                                 | Description                                                                                                            |
| :---------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------- |
| [get_invoice_list](#get_invoice_list)                                   | Retrieve a list of paid invoices for your workforce.                                                                   |
| [get_deel_invoice_list](#get_deel_invoice_list)                         | Retrieve a list of invoices related to Deel fees.                                                                      |
| [get_billing_invoice_download_link](#get_billing_invoice_download_link) | Get link to download the invoice PDF.                                                                                  |
| [get_payment_list](#get_payment_list)                                   | Retrieve a list of payments made to Deel.                                                                              |
| [get_payments_break_down_by_id](#get_payments_break_down_by_id)         | Get a full breakdown of a payment made to Deel. Breakdown will include individual invoices and Deel fee as line items. |

#### **get_invoice_list**

Retrieve a list of paid invoices for your workforce.

- HTTP Method: `GET`
- Endpoint: `/invoices`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| issued_from_date | str | ❌ | Retrieve a list of paid invoices for your workforce. |
| issued_to_date | str | ❌ | Retrieve a list of paid invoices for your workforce. |
| entities | GetInvoiceListEntities | ❌ | Retrieve a list of paid invoices for your workforce. |
| limit | float | ❌ | Retrieve a list of paid invoices for your workforce. |
| offset | float | ❌ | Retrieve a list of paid invoices for your workforce. |

**Return Type**

`InvoiceListContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import GetInvoiceListEntities

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
entities=GetInvoiceListEntities(**[
    "individual"
])

result = sdk.accounting.get_invoice_list(
    issued_from_date="issued_from_date",
    issued_to_date="issued_to_date",
    entities=entities,
    limit=10,
    offset=808037660.53
)

print(result)
```

#### **get_deel_invoice_list**

Retrieve a list of invoices related to Deel fees.

- HTTP Method: `GET`
- Endpoint: `/invoices/deel`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| contract_id | str | ✅ | Retrieve a list of invoices related to Deel fees. |
| limit | float | ❌ | Retrieve a list of invoices related to Deel fees. |
| offset | float | ❌ | Retrieve a list of invoices related to Deel fees. |

**Return Type**

`DeelInvoiceListContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.accounting.get_deel_invoice_list(
    contract_id="contract_id",
    limit=10,
    offset=237799437.03
)

print(result)
```

#### **get_billing_invoice_download_link**

Get link to download the invoice PDF.

- HTTP Method: `GET`
- Endpoint: `/invoices/{invoice_id}/download`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| invoice_id | str | ✅ | Get link to download the invoice PDF. |

**Return Type**

`InvoiceDownloadLinkContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.accounting.get_billing_invoice_download_link(invoice_id="invoice_id")

print(result)
```

#### **get_payment_list**

Retrieve a list of payments made to Deel.

- HTTP Method: `GET`
- Endpoint: `/payments`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| date_from | str | ❌ | Retrieve a list of payments made to Deel. |
| date_to | str | ❌ | Retrieve a list of payments made to Deel. |
| currencies | GetPaymentListCurrencies | ❌ | Retrieve a list of payments made to Deel. |
| entities | GetPaymentListEntities | ❌ | Retrieve a list of payments made to Deel. |

**Return Type**

`PaymentListContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import GetPaymentListCurrencies, GetPaymentListEntities

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
currencies=GetPaymentListCurrencies(**[
    "GBP"
])
entities=GetPaymentListEntities(**[
    "individual"
])

result = sdk.accounting.get_payment_list(
    date_from="1999-12-31",
    date_to="1999-12-31",
    currencies=currencies,
    entities=entities
)

print(result)
```

#### **get_payments_break_down_by_id**

Get a full breakdown of a payment made to Deel. Breakdown will include individual invoices and Deel fee as line items.

- HTTP Method: `GET`
- Endpoint: `/payments/{payment_id}/breakdown`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| payment_id | str | ✅ | Get a full breakdown of a payment made to Deel. Breakdown will include individual invoices and Deel fee as line items. |

**Return Type**

`PaymentBreakDownContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.accounting.get_payments_break_down_by_id(payment_id="payment_id")

print(result)
```

### ManagersService

A list of all methods in the `ManagersService` service. Click on the method name to view detailed information about that method.

| Methods                           | Description                        |
| :-------------------------------- | :--------------------------------- |
| [get_managers](#get_managers)     | List all organization managers.    |
| [create_manager](#create_manager) | Create a new organization manager. |

#### **get_managers**

List all organization managers.

- HTTP Method: `GET`
- Endpoint: `/managers`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| limit | str | ❌ | List all organization managers. |
| offset | str | ❌ | List all organization managers. |

**Return Type**

`AdminUsersContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.managers.get_managers(
    limit="50",
    offset="0"
)

print(result)
```

#### **create_manager**

Create a new organization manager.

- HTTP Method: `POST`
- Endpoint: `/managers`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | AdminUserCreateContainer | ✅ | The request body. |

**Return Type**

`CreateAdminUserResponseContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import AdminUserCreateContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = AdminUserCreateContainer(**{
    "data": {
        "first_name": "dolore",
        "last_name": "proi",
        "email": "email"
    }
})

result = sdk.managers.create_manager(request_body=request_body)

print(result)
```

### PeopleService

A list of all methods in the `PeopleService` service. Click on the method name to view detailed information about that method.

| Methods                                                                             | Description                                                                                                           |
| :---------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| [create_direct_employee](#create_direct_employee)                                   | Create a new Hris direct employee.                                                                                    |
| [get_internal_people_list](#get_internal_people_list)                               | Retrieve a list of internal people in your organization.                                                              |
| [get_people_list](#get_people_list)                                                 | Retrieve a list of People in your organization.                                                                       |
| [get_people_by_id](#get_people_by_id)                                               | Retrieve a single person in your organization.                                                                        |
| [update_people_department](#update_people_department)                               | Update worker department.                                                                                             |
| [update_people_working_location](#update_people_working_location)                   | Update worker working location.                                                                                       |
| [get_people](#get_people)                                                           | Retrieve the current user's profile.                                                                                  |
| [get_time_offs_for_employee](#get_time_offs_for_employee)                           | List of time offs by worker id. Worker id can be retreived using /people endpoint.                                    |
| [create_time_offs_for_employee](#create_time_offs_for_employee)                     | Add a time off request for a worker. New requests are auto-approved.                                                  |
| [get_time_offs_entitlements_for_employee](#get_time_offs_entitlements_for_employee) | Retrieve a list of time off entitlements for a worker.                                                                |
| [update_time_offs_for_employee](#update_time_offs_for_employee)                     | Edit a time off request for a worker.                                                                                 |
| [delete_time_offs_for_employee](#delete_time_offs_for_employee)                     | Delete a time off request.                                                                                            |
| [review_time_offs_for_employee](#review_time_offs_for_employee)                     | Approve or decline a time off request. New requests are auto-approved. Hence they don't need to be manually approved. |
| [get_time_offs_policies_for_employee](#get_time_offs_policies_for_employee)         | Retrieve a list of time off policies for a worker.                                                                    |

#### **create_direct_employee**

Create a new Hris direct employee.

- HTTP Method: `POST`
- Endpoint: `/hris/direct-employees`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | HrisDirectEmployee | ✅ | The request body. |

**Return Type**

`HrisDirectEmployeeContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import HrisDirectEmployee

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = HrisDirectEmployee(**{
    "employee_details": {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@domain.com",
        "work_email": "john.doe@domain.com",
        "nationality": "CA",
        "country": "BR",
        "state": "AC"
    },
    "team_information": {
        "team_id": 9.77,
        "legal_entity_id": 2.18
    },
    "job_information": {
        "seniority_id": 9.22,
        "job_title_id": 6.5
    },
    "compensation": {
        "gross_annual_salary": 7.15,
        "currency": "USD"
    },
    "contract": {
        "contract_oid": "pdcMQe0cXCCXWTkqkdytw",
        "start_date": "1999-12-31",
        "employee_number": 9.02,
        "end_date": "1999-12-31",
        "employment_type": "PART_TIME",
        "part_time_percentage": 21.67
    },
    "vacation_info": {
        "vacation_accrual_start_date": "vacation_accrual_start_date",
        "vacation_yearly_policy": 171.07
    }
})

result = sdk.people.create_direct_employee(request_body=request_body)

print(result)
```

#### **get_internal_people_list**

Retrieve a list of internal people in your organization.

- HTTP Method: `GET`
- Endpoint: `/internal/people`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| offset | float | ❌ | Retrieve a list of internal people in your organization. |
| limit | float | ❌ | Retrieve a list of internal people in your organization. |

**Return Type**

`InternalPeopleContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.people.get_internal_people_list(
    offset=978653984.34,
    limit=43.45
)

print(result)
```

#### **get_people_list**

Retrieve a list of People in your organization.

- HTTP Method: `GET`
- Endpoint: `/people`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| offset | float | ❌ | Retrieve a list of People in your organization. |
| limit | float | ❌ | Retrieve a list of People in your organization. |
| search | str | ❌ | Retrieve a list of People in your organization. |
| sort_by | PeopleSortByEnum | ❌ | Retrieve a list of People in your organization. |
| sort_order | SortDirEnum | ❌ | Retrieve a list of People in your organization. |
| hiring_statuses | HiringStatusEnum | ❌ | Retrieve a list of People in your organization. |

**Return Type**

`PeopleContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import PeopleSortByEnum, SortDirEnum, HiringStatusEnum

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.people.get_people_list(
    offset=44334375.53,
    limit=105.69,
    search="search",
    sort_by="id",
    sort_order="asc",
    hiring_statuses="active"
)

print(result)
```

#### **get_people_by_id**

Retrieve a single person in your organization.

- HTTP Method: `GET`
- Endpoint: `/people/{worker_id}`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| worker_id | str | ✅ | Retrieve a single person in your organization. |

**Return Type**

`PeopleByIdContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.people.get_people_by_id(worker_id="worker_id")

print(result)
```

#### **update_people_department**

Update worker department.

- HTTP Method: `PUT`
- Endpoint: `/people/{worker_id}/department`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | UpdateWorkerDepartmentContainer | ❌ | The request body. |
| worker_id | str | ✅ | Update worker department. |

**Return Type**

`GenericResultUpdated`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import UpdateWorkerDepartmentContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = UpdateWorkerDepartmentContainer(**{
    "data": {
        "department_id": "00000000-0000-0000-0000-000000000000"
    }
})

result = sdk.people.update_people_department(
    request_body=request_body,
    worker_id="worker_id"
)

print(result)
```

#### **update_people_working_location**

Update worker working location.

- HTTP Method: `PUT`
- Endpoint: `/people/{worker_id}/working-location`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | UpdateWorkerWorkingLocationContainer | ❌ | The request body. |
| worker_id | str | ✅ | Update worker working location. |

**Return Type**

`GenericResultUpdated`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import UpdateWorkerWorkingLocationContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = UpdateWorkerWorkingLocationContainer(**{
    "data": {
        "working_location_id": "00000000-0000-0000-0000-000000000000"
    }
})

result = sdk.people.update_people_working_location(
    request_body=request_body,
    worker_id="worker_id"
)

print(result)
```

#### **get_people**

Retrieve the current user's profile.

- HTTP Method: `GET`
- Endpoint: `/people/me`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|

**Return Type**

`PeopleMe`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.people.get_people()

print(result)
```

#### **get_time_offs_for_employee**

List of time offs by worker id. Worker id can be retreived using /people endpoint.

- HTTP Method: `GET`
- Endpoint: `/people/{worker_id}/time-offs`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| worker_id | str | ✅ | List of time offs by worker id. Worker id can be retreived using /people endpoint. |

**Return Type**

`EmployeeTimeoffsContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.people.get_time_offs_for_employee(worker_id="worker_id")

print(result)
```

#### **create_time_offs_for_employee**

Add a time off request for a worker. New requests are auto-approved.

- HTTP Method: `POST`
- Endpoint: `/people/{worker_id}/time-offs`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | dict | ❌ | The request body. |
| worker_id | str | ✅ | Add a time off request for a worker. New requests are auto-approved. |

**Return Type**

`EmployeeTimeoffsCreationContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import CreatePeopleTimeoff

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = {
    "type_": "VACATION",
    "start_date": "2022-09-03T00:00:00.000Z",
    "end_date": "2022-09-05T00:00:00.000Z",
    "reason": "Holiday",
    "attachments": "attachments"
}

result = sdk.people.create_time_offs_for_employee(
    request_body=request_body,
    worker_id="worker_id"
)

print(result)
```

#### **get_time_offs_entitlements_for_employee**

Retrieve a list of time off entitlements for a worker.

- HTTP Method: `GET`
- Endpoint: `/people/{worker_id}/time-offs/entitlements`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| worker_id | str | ✅ | Retrieve a list of time off entitlements for a worker. |

**Return Type**

`EmployeeTimeoffsEntitlementsContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.people.get_time_offs_entitlements_for_employee(worker_id="worker_id")

print(result)
```

#### **update_time_offs_for_employee**

Edit a time off request for a worker.

- HTTP Method: `PATCH`
- Endpoint: `/people/{worker_id}/time-offs/{timeoff_id}`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | dict | ❌ | The request body. |
| timeoff_id | str | ✅ | Edit a time off request for a worker. |
| worker_id | str | ✅ | Edit a time off request for a worker. |

**Return Type**

`EmployeeTimeoffsCreationContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import PeopleTimeOffContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = {
    "type_": "VACATION",
    "start_date": "2022-09-03T00:00:00.000Z",
    "end_date": "2022-09-05T00:00:00.000Z",
    "reason": "Holiday",
    "attachments": "attachments"
}

result = sdk.people.update_time_offs_for_employee(
    request_body=request_body,
    timeoff_id="timeoff_id",
    worker_id="worker_id"
)

print(result)
```

#### **delete_time_offs_for_employee**

Delete a time off request.

- HTTP Method: `DELETE`
- Endpoint: `/people/{worker_id}/time-offs/{timeoff_id}`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| timeoff_id | str | ✅ | Delete a time off request. |
| worker_id | str | ✅ | Delete a time off request. |

**Return Type**

`GenericResultDeleted`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.people.delete_time_offs_for_employee(
    timeoff_id="timeoff_id",
    worker_id="worker_id"
)

print(result)
```

#### **review_time_offs_for_employee**

Approve or decline a time off request. New requests are auto-approved. Hence they don't need to be manually approved.

- HTTP Method: `PATCH`
- Endpoint: `/people/{worker_id}/time-offs/{timeoff_id}/review`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | TimeoffToReviewInternalContainer | ✅ | The request body. |
| timeoff_id | str | ✅ | Approve or decline a time off request. New requests are auto-approved. Hence they don't need to be manually approved. |
| worker_id | str | ✅ | Approve or decline a time off request. New requests are auto-approved. Hence they don't need to be manually approved. |

**Return Type**

`EmployeeTimeoffsContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import TimeoffToReviewInternalContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = TimeoffToReviewInternalContainer(**{
    "data": {
        "status": "APPROVED",
        "reason": "Approved because there are no conflicts."
    }
})

result = sdk.people.review_time_offs_for_employee(
    request_body=request_body,
    timeoff_id="timeoff_id",
    worker_id="worker_id"
)

print(result)
```

#### **get_time_offs_policies_for_employee**

Retrieve a list of time off policies for a worker.

- HTTP Method: `GET`
- Endpoint: `/people/{worker_id}/time-offs/policies`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| worker_id | str | ✅ | Retrieve a list of time off policies for a worker. |

**Return Type**

`EmployeeTimeoffsPoliciesContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.people.get_time_offs_policies_for_employee(worker_id="worker_id")

print(result)
```

### EorService

A list of all methods in the `EorService` service. Click on the method name to view detailed information about that method.

| Methods                                                                     | Description                                                                                                                                                                       |
| :-------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [get_eor_country_validations](#get_eor_country_validations)                 | Retrieve the hiring guide data for a country. This data can be used to create Employee of Record (EOR) contract quotes.                                                           |
| [get_eor_worker_payslips](#get_eor_worker_payslips)                         | Get of payslips for an employee.                                                                                                                                                  |
| [get_eor_worker_payslip_download_url](#get_eor_worker_payslip_download_url) | Get download url for EOR payslip.                                                                                                                                                 |
| [calculate_eor_employment_cost](#calculate_eor_employment_cost)             | Determine EOR employee costs across the globe.                                                                                                                                    |
| [get_eor_contract_benefits](#get_eor_contract_benefits)                     | Retrieve EOR contract benefits                                                                                                                                                    |
| [create_eor_contract](#create_eor_contract)                                 | Create an Employee of Record (EOR) contract quote. The endpoints creates a contract quote request. Deel will process the information and get back with a quote for this contract. |

#### **get_eor_country_validations**

Retrieve the hiring guide data for a country. This data can be used to create Employee of Record (EOR) contract quotes.

- HTTP Method: `GET`
- Endpoint: `/eor/validations/{country_code}`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| country_code | str | ✅ | Retrieve the hiring guide data for a country. This data can be used to create Employee of Record (EOR) contract quotes. |

**Return Type**

`EorCountryValidationsContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.eor.get_eor_country_validations(country_code="US")

print(result)
```

#### **get_eor_worker_payslips**

Get of payslips for an employee.

- HTTP Method: `GET`
- Endpoint: `/eor/workers/{worker_id}/payslips`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| worker_id | str | ✅ | Get of payslips for an employee. |

**Return Type**

`EorPayslipsListContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.eor.get_eor_worker_payslips(worker_id="worker_id")

print(result)
```

#### **get_eor_worker_payslip_download_url**

Get download url for EOR payslip.

- HTTP Method: `GET`
- Endpoint: `/eor/workers/{worker_id}/payslips/{payslip_id}/download`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| worker_id | str | ✅ | Get download url for EOR payslip. |
| payslip_id | str | ✅ | Get download url for EOR payslip. |

**Return Type**

`EorPayslipDownloadUrlContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.eor.get_eor_worker_payslip_download_url(
    worker_id="worker_id",
    payslip_id="payslip_id"
)

print(result)
```

#### **calculate_eor_employment_cost**

Determine EOR employee costs across the globe.

- HTTP Method: `POST`
- Endpoint: `/eor/employment_cost`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | EorEmployeeCostCalculationRequestBodyContainer | ❌ | The request body. |

**Return Type**

`EorEmployeeCostCalculationResponseContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import EorEmployeeCostCalculationRequestBodyContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = EorEmployeeCostCalculationRequestBodyContainer(**{
    "data": {
        "salary": 50000,
        "country": "Germany",
        "currency": "EUR",
        "benefits": [
            {
                "provider_id": "00000000-0000-0000-0000-000000000000",
                "plan_id": "00000000-0000-0000-0000-000000000000"
            }
        ]
    }
})

result = sdk.eor.calculate_eor_employment_cost(request_body=request_body)

print(result)
```

#### **get_eor_contract_benefits**

Retrieve EOR contract benefits

- HTTP Method: `GET`
- Endpoint: `/eor/{contract_id}/benefits`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| contract_id | str | ✅ | Retrieve EOR contract benefits |

**Return Type**

`EorContractBenefitsContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.eor.get_eor_contract_benefits(contract_id="contract_id")

print(result)
```

#### **create_eor_contract**

Create an Employee of Record (EOR) contract quote. The endpoints creates a contract quote request. Deel will process the information and get back with a quote for this contract.

- HTTP Method: `POST`
- Endpoint: `/eor`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | EorContractToCreateContainer | ✅ | The request body. |

**Return Type**

`EorContractCreatedContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import EorContractToCreateContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = EorContractToCreateContainer(**{
    "data": {
        "employee": {
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "employee@email.com",
            "nationality": "US",
            "address": {
                "street": "Deel Street 500",
                "city": "Denver",
                "state": "CO",
                "zip": "44000",
                "country": "US"
            }
        },
        "employment": {
            "country": "US",
            "state": "state",
            "type_": "Full-time",
            "work_visa_required": False,
            "start_date": "1999-12-31",
            "end_date": "1999-12-31",
            "probation_period": 6.17,
            "scope_of_work": "scope_of_work",
            "time_off_type": "STANDARD",
            "holidays": 5.67
        },
        "job_title": "job_title",
        "seniority": {
            "id_": "00000000-0000-0000-0000-000000000000"
        },
        "client": {
            "legal_entity": {
                "id_": "00000000-0000-0000-0000-000000000000"
            },
            "team": {
                "id_": "00000000-0000-0000-0000-000000000000"
            }
        },
        "compensation_details": {
            "salary": 5.95,
            "currency": "currency",
            "variable_compensation": 3.49,
            "variable_compensation_type": "PERCENTAGE"
        },
        "quote_additional_fields": {
            "gender": "gender",
            "worker_type": "Skilled",
            "dob": "dob"
        },
        "health_plan_id": "health_plan_id",
        "pension": {
            "id_": "id",
            "contribution": "contribution"
        }
    }
})

result = sdk.eor.create_eor_contract(request_body=request_body)

print(result)
```

### GlobalPayrollService

A list of all methods in the `GlobalPayrollService` service. Click on the method name to view detailed information about that method.

| Methods                                                             | Description                                                                                                                             |
| :------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------- |
| [create_gp_contract](#create_gp_contract)                           | Create a Global Payroll contract.                                                                                                       |
| [get_worker_payslips](#get_worker_payslips)                         | Get of payslips for an employee.                                                                                                        |
| [update_gp_employee_address](#update_gp_employee_address)           | Update the address of a Global Payroll employee.                                                                                        |
| [get_gp_bank_accounts](#get_gp_bank_accounts)                       | Retrieve all bank accounts for an employee.                                                                                             |
| [add_gp_bank_account](#add_gp_bank_account)                         | Add a new bank account for an employee.                                                                                                 |
| [patch_gp_bank_account](#patch_gp_bank_account)                     | Modify bank account for an employee.                                                                                                    |
| [get_gp_bank_guide](#get_gp_bank_guide)                             | Retrieve the bank form guide for employee.                                                                                              |
| [update_gp_employee_compensation](#update_gp_employee_compensation) | Update the compensation of a Global Payroll employee. Returns the full compensation history including the update.                       |
| [update_gp_employee_pto](#update_gp_employee_pto)                   | Update the PTO policy of a Global Payroll employee.                                                                                     |
| [update_gp_employee_information](#update_gp_employee_information)   | Update Global Payroll employee information.                                                                                             |
| [get_download_url_for_gp_payslip](#get_download_url_for_gp_payslip) | Get download url for GP payslip.                                                                                                        |
| [get_gp_legal_entities](#get_gp_legal_entities)                     | Get list of global payroll events by legal entities.                                                                                    |
| [get_gross_to_net_gp_reports](#get_gross_to_net_gp_reports)         | Get list of global payroll reports detailing gross-to-net calculations.                                                                 |
| [download_gross_to_net_gp_report](#download_gross_to_net_gp_report) | Download global payroll reports detailing gross-to-net calculations.                                                                    |
| [request_termination](#request_termination)                         | Request a termination for a global payroll employee. A successful call starts the termination process and does not confirm termination. |

#### **create_gp_contract**

Create a Global Payroll contract.

- HTTP Method: `POST`
- Endpoint: `/contracts/gp`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | GpContractToCreateContainer | ✅ | The request body. |

**Return Type**

`GpContractCreatedContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import GpContractToCreateContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = GpContractToCreateContainer(**{
    "data": {
        "employee": {
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "culpa Lorem inc",
            "work_email": "in do L",
            "nationality": "US",
            "employee_number": "100",
            "address": {
                "street": "Deel Street 500",
                "city": "Denver",
                "state": "CO",
                "zip": "44000",
                "country": "US"
            }
        },
        "employment": {
            "type_": "Full-time",
            "start_date": "1999-12-31",
            "holidays": {
                "allowance": 5.28,
                "start_date": "1999-12-31"
            }
        },
        "job_title": "job_title",
        "client": {
            "legal_entity": {
                "id_": "00000000-0000-0000-0000-000000000000"
            },
            "team": {
                "id_": "00000000-0000-0000-0000-000000000000"
            }
        },
        "compensation_details": {
            "scale": "YEAR",
            "salary": 8.05,
            "currency": "GBP"
        }
    }
})

result = sdk.global_payroll.create_gp_contract(request_body=request_body)

print(result)
```

#### **get_worker_payslips**

Get of payslips for an employee.

- HTTP Method: `GET`
- Endpoint: `/gp/workers/{worker_id}/payslips`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| worker_id | str | ✅ | Get of payslips for an employee. |

**Return Type**

`GpPayslipsListContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.global_payroll.get_worker_payslips(worker_id="worker_id")

print(result)
```

#### **update_gp_employee_address**

Update the address of a Global Payroll employee.

- HTTP Method: `PATCH`
- Endpoint: `/gp/workers/{worker_id}/address`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | GpEmployeeAddressToUpdateContainer | ✅ | The request body. |
| worker_id | str | ✅ | Update the address of a Global Payroll employee. |

**Return Type**

`GpEmployeeAddressUpdatedContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import GpEmployeeAddressToUpdateContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = GpEmployeeAddressToUpdateContainer(**{
    "data": {
        "city": "London",
        "street": "123 Deel Street",
        "zip": "12345"
    }
})

result = sdk.global_payroll.update_gp_employee_address(
    request_body=request_body,
    worker_id="worker_id"
)

print(result)
```

#### **get_gp_bank_accounts**

Retrieve all bank accounts for an employee.

- HTTP Method: `GET`
- Endpoint: `/gp/workers/{worker_id}/banks`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| worker_id | str | ✅ | Retrieve all bank accounts for an employee. |

**Return Type**

`WorkerBankAccountsInfoContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.global_payroll.get_gp_bank_accounts(worker_id="worker_id")

print(result)
```

#### **add_gp_bank_account**

Add a new bank account for an employee.

- HTTP Method: `POST`
- Endpoint: `/gp/workers/{worker_id}/banks`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | AddWorkerBankAccountContainer | ✅ | The request body. |
| worker_id | str | ✅ | Add a new bank account for an employee. |

**Return Type**

`BankAccountUpdatedContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import AddWorkerBankAccountContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = AddWorkerBankAccountContainer(**{
    "data": {
        "full_name": "John Doe",
        "phone": "+1234567890",
        "address_line1": "1234 Main St",
        "address_line2": "Apartment 101",
        "city": "Springfield",
        "province_state": "Ontario",
        "postal": "12345",
        "bank_name": "Bank of Examples",
        "country_code": "US",
        "bank_country_code": "US",
        "swift_bic": "EXAMPLEBIC",
        "account_number": "123456789012",
        "bank_code": "123",
        "original_name": "Johnathan Doe",
        "tax_id": "123-45-6789",
        "branch_code": "001",
        "currency_code": "USD",
        "bank_branch_name": "Main Street Branch",
        "iban": "GB29NWBK60161331926819",
        "email": "john.doe@example.com",
        "rib_number": "12345678901",
        "account_type": "12345678901",
        "ach_routing_number": "12345678901"
    }
})

result = sdk.global_payroll.add_gp_bank_account(
    request_body=request_body,
    worker_id="worker_id"
)

print(result)
```

#### **patch_gp_bank_account**

Modify bank account for an employee.

- HTTP Method: `PATCH`
- Endpoint: `/gp/workers/{worker_id}/banks/{bank_id}`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | AddWorkerBankAccountContainer | ✅ | The request body. |
| worker_id | str | ✅ | Modify bank account for an employee. |
| bank_id | str | ✅ | Modify bank account for an employee. |

**Return Type**

`BankAccountUpdatedContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import AddWorkerBankAccountContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = AddWorkerBankAccountContainer(**{
    "data": {
        "full_name": "John Doe",
        "phone": "+1234567890",
        "address_line1": "1234 Main St",
        "address_line2": "Apartment 101",
        "city": "Springfield",
        "province_state": "Ontario",
        "postal": "12345",
        "bank_name": "Bank of Examples",
        "country_code": "US",
        "bank_country_code": "US",
        "swift_bic": "EXAMPLEBIC",
        "account_number": "123456789012",
        "bank_code": "123",
        "original_name": "Johnathan Doe",
        "tax_id": "123-45-6789",
        "branch_code": "001",
        "currency_code": "USD",
        "bank_branch_name": "Main Street Branch",
        "iban": "GB29NWBK60161331926819",
        "email": "john.doe@example.com",
        "rib_number": "12345678901",
        "account_type": "12345678901",
        "ach_routing_number": "12345678901"
    }
})

result = sdk.global_payroll.patch_gp_bank_account(
    request_body=request_body,
    worker_id="worker_id",
    bank_id="bank_id"
)

print(result)
```

#### **get_gp_bank_guide**

Retrieve the bank form guide for employee.

- HTTP Method: `GET`
- Endpoint: `/gp/workers/{worker_id}/banks/guide`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| worker_id | str | ✅ | Retrieve the bank form guide for employee. |

**Return Type**

`BankAccountGuideContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.global_payroll.get_gp_bank_guide(worker_id="worker_id")

print(result)
```

#### **update_gp_employee_compensation**

Update the compensation of a Global Payroll employee. Returns the full compensation history including the update.

- HTTP Method: `PATCH`
- Endpoint: `/gp/workers/{worker_id}/compensation`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | GpEmployeeCompensationToUpdateContainer | ✅ | The request body. |
| worker_id | str | ✅ | Update the compensation of a Global Payroll employee. Returns the full compensation history including the update. |

**Return Type**

`GpEmployeeCompensationUpdatedContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import GpEmployeeCompensationToUpdateContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = GpEmployeeCompensationToUpdateContainer(**{
    "data": {
        "scale": "YEAR",
        "salary": 50000,
        "effective_date": "1999-12-31"
    }
})

result = sdk.global_payroll.update_gp_employee_compensation(
    request_body=request_body,
    worker_id="worker_id"
)

print(result)
```

#### **update_gp_employee_pto**

Update the PTO policy of a Global Payroll employee.

- HTTP Method: `PATCH`
- Endpoint: `/gp/workers/{worker_id}/pto-policy`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | GpEmployeePtoToUpdateContainer | ✅ | The request body. |
| worker_id | str | ✅ | Update the PTO policy of a Global Payroll employee. |

**Return Type**

`GenericResultUpdated`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import GpEmployeePtoToUpdateContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = GpEmployeePtoToUpdateContainer(**{
    "data": {
        "accrual_start_date": "1999-12-31",
        "yearly_allowance": "15"
    }
})

result = sdk.global_payroll.update_gp_employee_pto(
    request_body=request_body,
    worker_id="worker_id"
)

print(result)
```

#### **update_gp_employee_information**

Update Global Payroll employee information.

- HTTP Method: `PATCH`
- Endpoint: `/gp/workers/{worker_id}/employee-information`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | GpEmployeeInformationToUpdateContainer | ✅ | The request body. |
| worker_id | str | ✅ | Update Global Payroll employee information. |

**Return Type**

`GpEmployeeInformationUpdatedContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import GpEmployeeInformationToUpdateContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = GpEmployeeInformationToUpdateContainer(**{
    "data": {
        "first_name": "Jane",
        "middle_name": "Jay",
        "last_name": "Doe",
        "date_of_birth": "1999-12-31",
        "gender": "gender",
        "marital_status": "Single",
        "employee_number": "employee_number"
    }
})

result = sdk.global_payroll.update_gp_employee_information(
    request_body=request_body,
    worker_id="worker_id"
)

print(result)
```

#### **get_download_url_for_gp_payslip**

Get download url for GP payslip.

- HTTP Method: `GET`
- Endpoint: `/gp/workers/{worker_id}/payslips/{payslip_id}/download`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| worker_id | str | ✅ | Get download url for GP payslip. |
| payslip_id | str | ✅ | Get download url for GP payslip. |

**Return Type**

`GpPayslipDownloadUrlContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.global_payroll.get_download_url_for_gp_payslip(
    worker_id="worker_id",
    payslip_id="payslip_id"
)

print(result)
```

#### **get_gp_legal_entities**

Get list of global payroll events by legal entities.

- HTTP Method: `GET`
- Endpoint: `/gp/legal-entities/{legal_entity_id}/reports`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| legal_entity_id | str | ✅ | Get list of global payroll events by legal entities. |
| start_date | str | ❌ | Get list of global payroll events by legal entities. |

**Return Type**

`GpPayrollEventReportContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.global_payroll.get_gp_legal_entities(
    legal_entity_id="legal_entity_id",
    start_date="1999-12-31"
)

print(result)
```

#### **get_gross_to_net_gp_reports**

Get list of global payroll reports detailing gross-to-net calculations.

- HTTP Method: `GET`
- Endpoint: `/gp/reports/{gp_report_id}/gross_to_net`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| gp_report_id | str | ✅ | Get list of global payroll reports detailing gross-to-net calculations. |

**Return Type**

`GlobalPayrollG2NReportContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.global_payroll.get_gross_to_net_gp_reports(gp_report_id="gp_report_id")

print(result)
```

#### **download_gross_to_net_gp_report**

Download global payroll reports detailing gross-to-net calculations.

- HTTP Method: `GET`
- Endpoint: `/gp/reports/{gp_report_id}/gross_to_net/csv`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| gp_report_id | str | ✅ | Download global payroll reports detailing gross-to-net calculations. |

**Return Type**

`str`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.global_payroll.download_gross_to_net_gp_report(gp_report_id="gp_report_id")

with open("output-file.txt", "w") as f:
    f.write(result)
```

#### **request_termination**

Request a termination for a global payroll employee. A successful call starts the termination process and does not confirm termination.

- HTTP Method: `POST`
- Endpoint: `/gp/workers/{worker_id}/terminations`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | WorkerTerminationBodyContainer | ✅ | The request body. |
| worker_id | str | ✅ | Request a termination for a global payroll employee. A successful call starts the termination process and does not confirm termination. |

**Return Type**

`WorkerTerminationContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import WorkerTerminationBodyContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = WorkerTerminationBodyContainer(**{
    "data": {
        "desired_end_date": "2023-12-31",
        "last_date_of_work": "2023-12-31",
        "message": "Termination reason",
        "is_voluntary": True,
        "severance": {}
    }
})

result = sdk.global_payroll.request_termination(
    request_body=request_body,
    worker_id="worker_id"
)

print(result)
```

### ContractorsService

A list of all methods in the `ContractorsService` service. Click on the method name to view detailed information about that method.

| Methods                                                             | Description                                                                                                                                                                                                   |
| :------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [create_contract_time_based](#create_contract_time_based)           | Create a new contract (time-based).                                                                                                                                                                           |
| [create_contract_task_based](#create_contract_task_based)           | Create a new Deel contract.                                                                                                                                                                                   |
| [create_contract_milestone_based](#create_contract_milestone_based) | Create a new Deel contract.                                                                                                                                                                                   |
| [create_contract_fixed_rate](#create_contract_fixed_rate)           | Create a new Deel contract.                                                                                                                                                                                   |
| [create_contract](#create_contract)                                 | Create a new Deel contract.                                                                                                                                                                                   |
| [get_contract_preview](#get_contract_preview)                       | Retrieve an IC and EOR contract agreement content in HTML. If no template is specified, the default or currently assigned template will be used. This endpoint does not support Global Payroll contract type. |
| [amend_contract_details](#amend_contract_details)                   | Amend the details of a contract. Please note that if the contract is already signed or active, then the update will have to be approved and re-signed for to take effect.                                     |
| [terminate_contract](#terminate_contract)                           | Terminate an active contract.                                                                                                                                                                                 |
| [add_premium](#add_premium)                                         | Add additional protection against misclassification by upgrading to Deel Premium.                                                                                                                             |
| [remove_premium_from_contract](#remove_premium_from_contract)       | Remove Deel Premium from an existing contract.                                                                                                                                                                |

#### **create_contract_time_based**

Create a new contract (time-based).

- HTTP Method: `POST`
- Endpoint: `/contracts/time-based`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | ContractToCreateContainerPayAsYouGoTimeBased | ✅ | The request body. |

**Return Type**

`ContractContainerPayAsYouGoTimeBased`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import ContractToCreateContainerPayAsYouGoTimeBased

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = ContractToCreateContainerPayAsYouGoTimeBased(**{
    "data": {
        "title": "title",
        "country_code": "US",
        "state_code": "state_code",
        "scope_of_work": "scope_of_work",
        "special_clause": "special_clause",
        "termination_date": "1999-12-31",
        "client": {
            "legal_entity": {
                "id_": "00000000-0000-0000-0000-000000000000"
            },
            "team": {
                "id_": "00000000-0000-0000-0000-000000000000"
            }
        },
        "job_title": {
            "id_": "00000000-0000-0000-0000-000000000000",
            "name": "sedDuis officia est laborum in"
        },
        "seniority": {
            "id_": "00000000-0000-0000-0000-000000000000"
        },
        "notice_period": 15,
        "who_reports": "both",
        "meta": {
            "documents_required": False,
            "is_main_income": False
        },
        "external_id": "external_id",
        "worker": {
            "expected_email": "occae",
            "first_name": "John",
            "last_name": "Doe"
        },
        "type_": "pay_as_you_go_time_based",
        "start_date": "1999-12-31",
        "compensation_details": {
            "amount": 2.6,
            "currency_code": "GBP",
            "frequency": "weekly",
            "cycle_end": 15,
            "cycle_end_type": "DAY_OF_WEEK",
            "payment_due_type": "REGULAR",
            "payment_due_days": 7,
            "pay_before_weekends": True,
            "first_payment_date": "1999-12-31",
            "first_payment": 500,
            "notice_period": 15,
            "scale": "hourly"
        }
    }
})

result = sdk.contractors.create_contract_time_based(request_body=request_body)

print(result)
```

#### **create_contract_task_based**

Create a new Deel contract.

- HTTP Method: `POST`
- Endpoint: `/contracts/task-based`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | ContractToCreateContainerPaygTasks | ✅ | The request body. |

**Return Type**

`ContractContainerPaygTasks`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import ContractToCreateContainerPaygTasks

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = ContractToCreateContainerPaygTasks(**{
    "data": {
        "title": "title",
        "country_code": "US",
        "state_code": "state_code",
        "scope_of_work": "scope_of_work",
        "special_clause": "special_clause",
        "termination_date": "1999-12-31",
        "client": {
            "legal_entity": {
                "id_": "00000000-0000-0000-0000-000000000000"
            },
            "team": {
                "id_": "00000000-0000-0000-0000-000000000000"
            }
        },
        "job_title": {
            "id_": "00000000-0000-0000-0000-000000000000",
            "name": "enim irure dolore magna"
        },
        "seniority": {
            "id_": "00000000-0000-0000-0000-000000000000"
        },
        "notice_period": 15,
        "who_reports": "both",
        "meta": {
            "documents_required": False,
            "is_main_income": False
        },
        "external_id": "external_id",
        "worker": {
            "expected_email": "Duis nulla oc",
            "first_name": "John",
            "last_name": "Doe"
        },
        "type_": "payg_tasks",
        "start_date": "1999-12-31",
        "compensation_details": {
            "amount": 100,
            "currency_code": "GBP",
            "frequency": "weekly",
            "cycle_end": 15,
            "cycle_end_type": "DAY_OF_WEEK",
            "payment_due_type": "REGULAR",
            "payment_due_days": 7,
            "pay_before_weekends": True,
            "first_payment_date": "1999-12-31",
            "first_payment": 500,
            "notice_period": 15
        }
    }
})

result = sdk.contractors.create_contract_task_based(request_body=request_body)

print(result)
```

#### **create_contract_milestone_based**

Create a new Deel contract.

- HTTP Method: `POST`
- Endpoint: `/contracts/milestone-based`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | ContractToCreateContainerPaygMilestones | ✅ | The request body. |

**Return Type**

`ContractContainerPaygMilestones`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import ContractToCreateContainerPaygMilestones

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = ContractToCreateContainerPaygMilestones(**{
    "data": {
        "title": "title",
        "country_code": "US",
        "state_code": "state_code",
        "scope_of_work": "scope_of_work",
        "special_clause": "special_clause",
        "termination_date": "1999-12-31",
        "client": {
            "legal_entity": {
                "id_": "00000000-0000-0000-0000-000000000000"
            },
            "team": {
                "id_": "00000000-0000-0000-0000-000000000000"
            }
        },
        "job_title": {
            "id_": "00000000-0000-0000-0000-000000000000",
            "name": "et dolore"
        },
        "seniority": {
            "id_": "00000000-0000-0000-0000-000000000000"
        },
        "notice_period": 15,
        "who_reports": "both",
        "meta": {
            "documents_required": False,
            "is_main_income": False
        },
        "external_id": "external_id",
        "worker": {
            "expected_email": "sint ",
            "first_name": "John",
            "last_name": "Doe"
        },
        "type_": "payg_milestones",
        "start_date": "1999-12-31",
        "compensation_details": {
            "amount": 100,
            "currency_code": "GBP",
            "frequency": "weekly",
            "cycle_end": 15,
            "cycle_end_type": "DAY_OF_WEEK",
            "payment_due_type": "REGULAR",
            "payment_due_days": 7,
            "pay_before_weekends": True,
            "first_payment_date": "1999-12-31",
            "first_payment": 500,
            "notice_period": 15
        }
    }
})

result = sdk.contractors.create_contract_milestone_based(request_body=request_body)

print(result)
```

#### **create_contract_fixed_rate**

Create a new Deel contract.

- HTTP Method: `POST`
- Endpoint: `/contracts/fixed-rate`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | ContractToCreateContainerOngoingTimeBased | ✅ | The request body. |

**Return Type**

`ContractContainerOngoingTimeBased`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import ContractToCreateContainerOngoingTimeBased

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = ContractToCreateContainerOngoingTimeBased(**{
    "data": {
        "title": "title",
        "country_code": "US",
        "state_code": "state_code",
        "scope_of_work": "scope_of_work",
        "special_clause": "special_clause",
        "termination_date": "1999-12-31",
        "client": {
            "legal_entity": {
                "id_": "00000000-0000-0000-0000-000000000000"
            },
            "team": {
                "id_": "00000000-0000-0000-0000-000000000000"
            }
        },
        "job_title": {
            "id_": "00000000-0000-0000-0000-000000000000",
            "name": "cillum"
        },
        "seniority": {
            "id_": "00000000-0000-0000-0000-000000000000"
        },
        "notice_period": 15,
        "who_reports": "both",
        "meta": {
            "documents_required": False,
            "is_main_income": False
        },
        "external_id": "external_id",
        "worker": {
            "expected_email": "Lorem sint et",
            "first_name": "John",
            "last_name": "Doe"
        },
        "type_": "ongoing_time_based",
        "start_date": "1999-12-31",
        "compensation_details": {
            "amount": 7.36,
            "currency_code": "GBP",
            "frequency": "weekly",
            "cycle_end": 15,
            "cycle_end_type": "DAY_OF_WEEK",
            "payment_due_type": "REGULAR",
            "payment_due_days": 7,
            "pay_before_weekends": True,
            "first_payment_date": "1999-12-31",
            "first_payment": 500,
            "notice_period": 15,
            "scale": "hourly"
        }
    }
})

result = sdk.contractors.create_contract_fixed_rate(request_body=request_body)

print(result)
```

#### **create_contract**

Create a new Deel contract.

- HTTP Method: `POST`
- Endpoint: `/contracts`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | ContractToCreateContainer | ✅ | The request body. |

**Return Type**

`ContractContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import ContractToCreateContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = ContractToCreateContainer(**{
    "data": {
        "title": "title",
        "country_code": "US",
        "state_code": "state_code",
        "scope_of_work": "scope_of_work",
        "special_clause": "special_clause",
        "termination_date": "1999-12-31",
        "client": {
            "legal_entity": {
                "id_": "00000000-0000-0000-0000-000000000000"
            },
            "team": {
                "id_": "00000000-0000-0000-0000-000000000000"
            }
        },
        "job_title": {
            "id_": "00000000-0000-0000-0000-000000000000",
            "name": "sedDuis officia est laborum in"
        },
        "seniority": {
            "id_": "00000000-0000-0000-0000-000000000000"
        },
        "notice_period": 15,
        "who_reports": "both",
        "meta": {
            "documents_required": False,
            "is_main_income": False
        },
        "external_id": "external_id",
        "worker": {
            "expected_email": "occae",
            "first_name": "John",
            "last_name": "Doe"
        },
        "type_": "pay_as_you_go_time_based",
        "start_date": "1999-12-31",
        "compensation_details": {
            "amount": 2.6,
            "currency_code": "GBP",
            "frequency": "weekly",
            "cycle_end": 15,
            "cycle_end_type": "DAY_OF_WEEK",
            "payment_due_type": "REGULAR",
            "payment_due_days": 7,
            "pay_before_weekends": True,
            "first_payment_date": "1999-12-31",
            "first_payment": 500,
            "notice_period": 15,
            "scale": "hourly"
        }
    }
})

result = sdk.contractors.create_contract(request_body=request_body)

print(result)
```

#### **get_contract_preview**

Retrieve an IC and EOR contract agreement content in HTML. If no template is specified, the default or currently assigned template will be used. This endpoint does not support Global Payroll contract type.

- HTTP Method: `GET`
- Endpoint: `/contracts/{contract_id}/preview`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| contract_id | str | ✅ | Retrieve an IC and EOR contract agreement content in HTML. If no template is specified, the default or currently assigned template will be used. This endpoint does not support Global Payroll contract type. |
| template_id | str | ❌ | Retrieve an IC and EOR contract agreement content in HTML. If no template is specified, the default or currently assigned template will be used. This endpoint does not support Global Payroll contract type. |

**Return Type**

`str`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.contractors.get_contract_preview(
    contract_id="contract_id",
    template_id="templateId"
)

with open("output-file.html", "w") as f:
    f.write(result)
```

#### **amend_contract_details**

Amend the details of a contract. Please note that if the contract is already signed or active, then the update will have to be approved and re-signed for to take effect.

- HTTP Method: `POST`
- Endpoint: `/contracts/{contract_id}/amendments`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | ContractToAmendDetailsContainer | ✅ | The request body. |
| contract_id | str | ✅ | Amend the details of a contract. Please note that if the contract is already signed or active, then the update will have to be approved and re-signed for to take effect. |

**Return Type**

`GenericResultCreated`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import ContractToAmendDetailsContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = ContractToAmendDetailsContainer(**{
    "data": {
        "amount": 100,
        "currency_code": "GBP",
        "scale": "hourly",
        "effective_date": "1999-12-31",
        "first_payment_date": "1999-12-31",
        "first_payment": 0.24,
        "frequency": "weekly",
        "cycle_end": 24.94,
        "cycle_end_type": "DAY_OF_WEEK",
        "payment_due_type": "REGULAR",
        "payment_due_days": 0.92,
        "pay_before_weekends": True,
        "job_title_name": "3D Designer",
        "job_title_id": "00000000-0000-0000-0000-000000000000",
        "seniority_id": "00000000-0000-0000-0000-000000000000",
        "special_clause": "special_clause",
        "scope_of_work": "scope_of_work"
    }
})

result = sdk.contractors.amend_contract_details(
    request_body=request_body,
    contract_id="contract_id"
)

print(result)
```

#### **terminate_contract**

Terminate an active contract.

- HTTP Method: `POST`
- Endpoint: `/contracts/{contract_id}/terminations`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | ContractToTerminateContainer | ✅ | The request body. |
| contract_id | str | ✅ | Terminate an active contract. |

**Return Type**

`ContractTerminationResultContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import ContractToTerminateContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = ContractToTerminateContainer(**{
    "data": {
        "completion_date": "1999-12-31",
        "terminate_now": True,
        "message": "message"
    }
})

result = sdk.contractors.terminate_contract(
    request_body=request_body,
    contract_id="contract_id"
)

print(result)
```

#### **add_premium**

Add additional protection against misclassification by upgrading to Deel Premium.

- HTTP Method: `POST`
- Endpoint: `/contracts/{contract_id}/premium`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | PremiumToAddContainer | ❌ | The request body. |
| contract_id | str | ✅ | Add additional protection against misclassification by upgrading to Deel Premium. |

**Return Type**

`PremiumResultAddedContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import PremiumToAddContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = PremiumToAddContainer(**{
    "data": {
        "agreement_reflects_relation": True,
        "contractor_characteristics": True
    }
})

result = sdk.contractors.add_premium(
    request_body=request_body,
    contract_id="contract_id"
)

print(result)
```

#### **remove_premium_from_contract**

Remove Deel Premium from an existing contract.

- HTTP Method: `DELETE`
- Endpoint: `/contracts/{contract_id}/premium`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| contract_id | str | ✅ | Remove Deel Premium from an existing contract. |
| reason | str | ❌ | Remove Deel Premium from an existing contract. |

**Return Type**

`GenericResultDeleted`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.contractors.remove_premium_from_contract(
    contract_id="contract_id",
    reason="reason"
)

print(result)
```

### AdjustmentsService

A list of all methods in the `AdjustmentsService` service. Click on the method name to view detailed information about that method.

| Methods                                         | Description                                                                         |
| :---------------------------------------------- | :---------------------------------------------------------------------------------- |
| [create_adjustment](#create_adjustment)         | Create a new adjustment.                                                            |
| [get_adjustments_by_id](#get_adjustments_by_id) | Retrieve an adjustment.                                                             |
| [update_adjustment](#update_adjustment)         | Update an adjustment.                                                               |
| [delete_adjustment](#delete_adjustment)         | Delete an adjustment.                                                               |
| [get_categories](#get_categories)               | Get all categories for your organization.                                           |
| [create_file_ref](#create_file_ref)             | Upload file to Deel storage to use the file attachment feature for other endpoints. |
| [get_adjustments](#get_adjustments)             | Get all adjustments for the specific contract.                                      |

#### **create_adjustment**

Create a new adjustment.

- HTTP Method: `POST`
- Endpoint: `/adjustments`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | dict | ✅ | The request body. |

**Return Type**

`AdjustmentCreatedContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import AdjustmentToCreateContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = {
    "data": {
        "contract_id": "m3jk2j",
        "amount": "cupidatat exe",
        "date_of_adjustment": "1999-12-31",
        "title": "Your title here",
        "description": "Your description here",
        "cycle_reference": "my_cycle_reference",
        "file": "qu",
        "adjustment_category_id": "c9cf4c2c0165f48f494415390c3b49",
        "move_next_cycle": True,
        "vendor": "Vendor",
        "country": "US"
    }
}

result = sdk.adjustments.create_adjustment(request_body=request_body)

print(result)
```

#### **get_adjustments_by_id**

Retrieve an adjustment.

- HTTP Method: `GET`
- Endpoint: `/adjustments/{adjustment_id}`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| adjustment_id | str | ✅ | Retrieve an adjustment. |

**Return Type**

`AdjustmentCreatedContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.adjustments.get_adjustments_by_id(adjustment_id="adjustment_id")

print(result)
```

#### **update_adjustment**

Update an adjustment.

- HTTP Method: `PATCH`
- Endpoint: `/adjustments/{adjustment_id}`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | AdjustmentToUpdateContainer | ✅ | The request body. |
| adjustment_id | str | ✅ | Update an adjustment. |

**Return Type**

`GenericResultUpdated`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import AdjustmentToUpdateContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = AdjustmentToUpdateContainer(**{
    "data": {
        "amount": "ut velit in",
        "title": "Your title here",
        "description": "Your description here",
        "file": "incididunt "
    }
})

result = sdk.adjustments.update_adjustment(
    request_body=request_body,
    adjustment_id="adjustment_id"
)

print(result)
```

#### **delete_adjustment**

Delete an adjustment.

- HTTP Method: `DELETE`
- Endpoint: `/adjustments/{adjustment_id}`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| adjustment_id | str | ✅ | Delete an adjustment. |

**Return Type**

`GenericResultDeleted`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.adjustments.delete_adjustment(adjustment_id="adjustment_id")

print(result)
```

#### **get_categories**

Get all categories for your organization.

- HTTP Method: `GET`
- Endpoint: `/adjustments/categories`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|

**Return Type**

`AdjustmentsCategoriesContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.adjustments.get_categories()

print(result)
```

#### **create_file_ref**

Upload file to Deel storage to use the file attachment feature for other endpoints.

- HTTP Method: `POST`
- Endpoint: `/attachments`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | InputToCreateFileRef | ✅ | The request body. |

**Return Type**

`OutputToCreateFileRefContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import InputToCreateFileRef

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = InputToCreateFileRef(**{
    "data": {
        "content_type": "application/pdf"
    }
})

result = sdk.adjustments.create_file_ref(request_body=request_body)

print(result)
```

#### **get_adjustments**

Get all adjustments for the specific contract.

- HTTP Method: `GET`
- Endpoint: `/contracts/{contract_id}/adjustments`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| contract*id | str | ✅ | Get all adjustments for the specific contract. |
| from* | str | ❌ | Get all adjustments for the specific contract. |
| to | str | ❌ | Get all adjustments for the specific contract. |

**Return Type**

`AdjustmentsContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.adjustments.get_adjustments(
    contract_id="contract_id",
    from_="from",
    to="to"
)

print(result)
```

### CandidatesService

A list of all methods in the `CandidatesService` service. Click on the method name to view detailed information about that method.

| Methods                             | Description                  |
| :---------------------------------- | :--------------------------- |
| [add_candidate](#add_candidate)     | Add a candidate to Deel.     |
| [patch_candidate](#patch_candidate) | Update an existed candidate. |

#### **add_candidate**

Add a candidate to Deel.

- HTTP Method: `POST`
- Endpoint: `/candidates`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | CandidateToCreateContainer | ✅ | The request body. |

**Return Type**

`GenericResultCreated`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import CandidateToCreateContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CandidateToCreateContainer(**{
    "data": {
        "id_": "id",
        "first_name": "John",
        "last_name": "Doe",
        "status": "offer-accepted",
        "start_date": "1999-12-31",
        "link": "link",
        "job_title": "3D Designer",
        "email": "dolore",
        "nationality": "US",
        "country": "US",
        "state": "AL"
    }
})

result = sdk.candidates.add_candidate(request_body=request_body)

print(result)
```

#### **patch_candidate**

Update an existed candidate.

- HTTP Method: `PATCH`
- Endpoint: `/candidates/{candidate_id}`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | CandidateToPatchContainer | ✅ | The request body. |
| candidate_id | str | ✅ | Update an existed candidate. |

**Return Type**

`GenericResultUpdated`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import CandidateToPatchContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CandidateToPatchContainer(**{
    "data": {
        "first_name": "John",
        "last_name": "Doe",
        "status": "offer-accepted",
        "start_date": "1999-12-31",
        "job_title": "3D Designer",
        "link": "link",
        "email": "Excepteur nu",
        "nationality": "US",
        "country": "US",
        "state": "AL"
    }
})

result = sdk.candidates.patch_candidate(
    request_body=request_body,
    candidate_id="candidate_id"
)

print(result)
```

### PartnerManagedService

A list of all methods in the `PartnerManagedService` service. Click on the method name to view detailed information about that method.

| Methods                                                                                           | Description                                                                                                            |
| :------------------------------------------------------------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------- |
| [add_employee_additional_information](#add_employee_additional_information)                       | Add additional information for an EOR employee.                                                                        |
| [sign_employee_contract](#sign_employee_contract)                                                 | Sign a contract as a employee.                                                                                         |
| [request_custom_verification_letter](#request_custom_verification_letter)                         | Request employment verification letters, visa support, bank verification and more.                                     |
| [get_hr_verification_letters_and_documents](#get_hr_verification_letters_and_documents)           | List all HR verification letters and documents available.                                                              |
| [download_hr_verification_letters_and_documents](#download_hr_verification_letters_and_documents) | Retrieve URL to download HR verification letters and documents.                                                        |
| [get_offer_letter_preview](#get_offer_letter_preview)                                             | Retrieve an EOR job offer letter in HTML. This endpoint does not support IC and Global Payroll contract types.         |
| [get_employee_agreement_preview](#get_employee_agreement_preview)                                 | Retrieve an EOR Employee Agreement content in HTML.                                                                    |
| [get_employee_agreement_download_link](#get_employee_agreement_download_link)                     | Get link to download the employee agreement PDF.                                                                       |
| [get_bank_account_guide](#get_bank_account_guide)                                                 | Retrieve bank account form guide for an EOR employee. This data can be used to add a new bank account for an employee. |
| [add_bank_account](#add_bank_account)                                                             | Add bank account for an EOR employee.                                                                                  |
| [patch_bank_account](#patch_bank_account)                                                         | Modify bank account for an EOR employee.                                                                               |
| [get_employee_payslips](#get_employee_payslips)                                                   | Get list of payslips for an EOR employee.                                                                              |
| [get_employee_compliance_documents](#get_employee_compliance_documents)                           | Get a list of employee compliance documents.                                                                           |
| [upload_employee_compliance_document](#upload_employee_compliance_document)                       | Upload an employee compliance document.                                                                                |
| [get_employee_compliance_document_template](#get_employee_compliance_document_template)           | Get the download link for an employee compliance document template, if it exists.                                      |
| [get_employee_tax_documents](#get_employee_tax_documents)                                         | Get list of tax documents for an employee.                                                                             |

#### **add_employee_additional_information**

Add additional information for an EOR employee.

- HTTP Method: `POST`
- Endpoint: `/partner-managed/employees/{employee_id}/contracts/{contract_id}/additional-information`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | AdditionalEorInfoContainer | ✅ | The request body. |
| employee_id | str | ✅ | Add additional information for an EOR employee. |
| contract_id | str | ✅ | Add additional information for an EOR employee. |

**Return Type**

`GenericResultUpdated`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import AdditionalEorInfoContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = AdditionalEorInfoContainer(**{
    "data": ""
})

result = sdk.partner_managed.add_employee_additional_information(
    request_body=request_body,
    employee_id="employee_id",
    contract_id="contract_id"
)

print(result)
```

#### **sign_employee_contract**

Sign a contract as a employee.

- HTTP Method: `POST`
- Endpoint: `/partner-managed/employees/{employee_id}/contracts/{contract_id}/signatures`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | EmployeeContractSignatureToCreateContainer | ✅ | The request body. |
| employee_id | str | ✅ | Sign a contract as a employee. |
| contract_id | str | ✅ | Sign a contract as a employee. |

**Return Type**

`GenericResultCreated`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import EmployeeContractSignatureToCreateContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = EmployeeContractSignatureToCreateContainer(**{
    "data": {
        "signature": "aliqua sed comm"
    }
})

result = sdk.partner_managed.sign_employee_contract(
    request_body=request_body,
    employee_id="employee_id",
    contract_id="contract_id"
)

print(result)
```

#### **request_custom_verification_letter**

Request employment verification letters, visa support, bank verification and more.

- HTTP Method: `POST`
- Endpoint: `/partner-managed/employees/{employee_id}/contracts/{contract_id}/custom-verification-letter`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | RequestCustomVerificationLetterContainer | ✅ | The request body. |
| employee_id | str | ✅ | Request employment verification letters, visa support, bank verification and more. |
| contract_id | str | ✅ | Request employment verification letters, visa support, bank verification and more. |

**Return Type**

`GenericResultCreated`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import RequestCustomVerificationLetterContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = RequestCustomVerificationLetterContainer(**{
    "data": {
        "description": "magnaest ea con",
        "include_qr_code": True,
        "type_": "VISA_APPLICATION_FOR_PERSONAL_TRIP"
    }
})

result = sdk.partner_managed.request_custom_verification_letter(
    request_body=request_body,
    employee_id="employee_id",
    contract_id="contract_id"
)

print(result)
```

#### **get_hr_verification_letters_and_documents**

List all HR verification letters and documents available.

- HTTP Method: `GET`
- Endpoint: `/partner-managed/employees/{employee_id}/contracts/{contract_id}/hr-documents`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| employee_id | str | ✅ | List all HR verification letters and documents available. |
| contract_id | str | ✅ | List all HR verification letters and documents available. |

**Return Type**

`HrVerificationLettersAndDocumentsListContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.partner_managed.get_hr_verification_letters_and_documents(
    employee_id="employee_id",
    contract_id="contract_id"
)

print(result)
```

#### **download_hr_verification_letters_and_documents**

Retrieve URL to download HR verification letters and documents.

- HTTP Method: `GET`
- Endpoint: `/partner-managed/employees/{employee_id}/contracts/{contract_id}/hr-documents/{document_id}/download`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| employee_id | str | ✅ | Retrieve URL to download HR verification letters and documents. |
| contract_id | str | ✅ | Retrieve URL to download HR verification letters and documents. |
| document_id | float | ✅ | Retrieve URL to download HR verification letters and documents. |

**Return Type**

`EmployeeAgreementDownloadContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.partner_managed.download_hr_verification_letters_and_documents(
    employee_id="employee_id",
    contract_id="contract_id",
    document_id=1.72
)

print(result)
```

#### **get_offer_letter_preview**

Retrieve an EOR job offer letter in HTML. This endpoint does not support IC and Global Payroll contract types.

- HTTP Method: `GET`
- Endpoint: `/partner-managed/employees/{employee_id}/contracts/{contract_id}/offer-letter`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| employee_id | str | ✅ | Retrieve an EOR job offer letter in HTML. This endpoint does not support IC and Global Payroll contract types. |
| contract_id | str | ✅ | Retrieve an EOR job offer letter in HTML. This endpoint does not support IC and Global Payroll contract types. |

**Return Type**

`str`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.partner_managed.get_offer_letter_preview(
    employee_id="employee_id",
    contract_id="contract_id"
)

with open("output-file.html", "w") as f:
    f.write(result)
```

#### **get_employee_agreement_preview**

Retrieve an EOR Employee Agreement content in HTML.

- HTTP Method: `GET`
- Endpoint: `/partner-managed/employees/{employee_id}/contracts/{contract_id}/employee-agreement`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| employee_id | str | ✅ | Retrieve an EOR Employee Agreement content in HTML. |
| contract_id | str | ✅ | Retrieve an EOR Employee Agreement content in HTML. |

**Return Type**

`str`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.partner_managed.get_employee_agreement_preview(
    employee_id="employee_id",
    contract_id="contract_id"
)

with open("output-file.html", "w") as f:
    f.write(result)
```

#### **get_employee_agreement_download_link**

Get link to download the employee agreement PDF.

- HTTP Method: `GET`
- Endpoint: `/partner-managed/employees/{employee_id}/contracts/{contract_id}/employee-agreement/download`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| employee_id | str | ✅ | Get link to download the employee agreement PDF. |
| contract_id | str | ✅ | Get link to download the employee agreement PDF. |

**Return Type**

`EmployeeAgreementDownloadContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.partner_managed.get_employee_agreement_download_link(
    employee_id="employee_id",
    contract_id="contract_id"
)

print(result)
```

#### **get_bank_account_guide**

Retrieve bank account form guide for an EOR employee. This data can be used to add a new bank account for an employee.

- HTTP Method: `GET`
- Endpoint: `/partner-managed/employees/{employee_id}/banks/guide`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| employee_id | str | ✅ | Retrieve bank account form guide for an EOR employee. This data can be used to add a new bank account for an employee. |

**Return Type**

`BankAccountGuideContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.partner_managed.get_bank_account_guide(employee_id="employee_id")

print(result)
```

#### **add_bank_account**

Add bank account for an EOR employee.

- HTTP Method: `POST`
- Endpoint: `/partner-managed/employees/{employee_id}/banks`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | BankAccountToAddContainer | ✅ | The request body. |
| employee_id | str | ✅ | Add bank account for an EOR employee. |

**Return Type**

`BankAccountAddedContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import BankAccountToAddContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = BankAccountToAddContainer(**{
    "data": [
        {
            "key": "key",
            "value": "value"
        }
    ]
})

result = sdk.partner_managed.add_bank_account(
    request_body=request_body,
    employee_id="employee_id"
)

print(result)
```

#### **patch_bank_account**

Modify bank account for an EOR employee.

- HTTP Method: `PATCH`
- Endpoint: `/partner-managed/employees/{employee_id}/banks/{bank_id}`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | BankAccountToAddContainer | ✅ | The request body. |
| employee_id | str | ✅ | Modify bank account for an EOR employee. |
| bank_id | str | ✅ | Modify bank account for an EOR employee. |

**Return Type**

`BankAccountAddedContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import BankAccountToAddContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = BankAccountToAddContainer(**{
    "data": [
        {
            "key": "key",
            "value": "value"
        }
    ]
})

result = sdk.partner_managed.patch_bank_account(
    request_body=request_body,
    employee_id="employee_id",
    bank_id="bank_id"
)

print(result)
```

#### **get_employee_payslips**

Get list of payslips for an EOR employee.

- HTTP Method: `GET`
- Endpoint: `/partner-managed/employees/{employee_id}/payslips`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| employee_id | str | ✅ | Get list of payslips for an EOR employee. |

**Return Type**

`EmployeePayslipsListContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.partner_managed.get_employee_payslips(employee_id="employee_id")

print(result)
```

#### **get_employee_compliance_documents**

Get a list of employee compliance documents.

- HTTP Method: `GET`
- Endpoint: `/partner-managed/employees/{employee_id}/compliance-documents`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| employee_id | str | ✅ | Get a list of employee compliance documents. |

**Return Type**

`GetEmployeeComplianceDocumentsContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.partner_managed.get_employee_compliance_documents(employee_id="employee_id")

print(result)
```

#### **upload_employee_compliance_document**

Upload an employee compliance document.

- HTTP Method: `POST`
- Endpoint: `/partner-managed/employees/{employee_id}/compliance-documents/{document_id}`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | dict | ✅ | The request body. |
| employee_id | str | ✅ | Upload an employee compliance document. |
| document_id | float | ✅ | Upload an employee compliance document. |

**Return Type**

`UploadEmployeeComplianceDocumentContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import UploadEmployeeComplianceDocumentFileContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = {
    "file": "file"
}

result = sdk.partner_managed.upload_employee_compliance_document(
    request_body=request_body,
    employee_id="employee_id",
    document_id=1.36
)

print(result)
```

#### **get_employee_compliance_document_template**

Get the download link for an employee compliance document template, if it exists.

- HTTP Method: `GET`
- Endpoint: `/partner-managed/employees/{employee_id}/compliance-documents/{document_id}/templates/download`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| employee_id | str | ✅ | Get the download link for an employee compliance document template, if it exists. |
| document_id | float | ✅ | Get the download link for an employee compliance document template, if it exists. |

**Return Type**

`GetEmployeeComplianceDocumentTemplateDownloadLinkContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.partner_managed.get_employee_compliance_document_template(
    employee_id="employee_id",
    document_id=5.91
)

print(result)
```

#### **get_employee_tax_documents**

Get list of tax documents for an employee.

- HTTP Method: `GET`
- Endpoint: `/partner-managed/employees/{employee_id}/tax-documents`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| employee_id | str | ✅ | Get list of tax documents for an employee. |

**Return Type**

`EmployeeTaxDocumentsListContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.partner_managed.get_employee_tax_documents(employee_id="employee_id")

print(result)
```

### ContractsService

A list of all methods in the `ContractsService` service. Click on the method name to view detailed information about that method.

| Methods                                                                     | Description                                                                                                                                                                                                          |
| :-------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [get_contract_list](#get_contract_list)                                     | Retrieve a list of contracts.                                                                                                                                                                                        |
| [get_contract_by_id](#get_contract_by_id)                                   | Retrieve a single contract.                                                                                                                                                                                          |
| [attach_external_id](#attach_external_id)                                   | Add an external Id to a Deel contract. You can use this to add a Deel contract's refernece Id in your platform. External Id can be passed as a query parameter in List contract endpoint to find this conract later. |
| [add_contract_document](#add_contract_document)                             | Attach a file to contract document.                                                                                                                                                                                  |
| [edit_contract_document](#edit_contract_document)                           | Overwrite the file currently attached to contract document.                                                                                                                                                          |
| [get_alternate_emails_by_contract_id](#get_alternate_emails_by_contract_id) | Returns an array of alternate email objects                                                                                                                                                                          |
| [sign_contract](#sign_contract)                                             | Sign a contract as a client.                                                                                                                                                                                         |
| [invite_to_sign_contract](#invite_to_sign_contract)                         | Invite a worker to sign the contract. Worker will be notified via email.                                                                                                                                             |
| [uninvite_to_sign_contract](#uninvite_to_sign_contract)                     | Remove invite in order to re-invite a worker to sign the contract.                                                                                                                                                   |
| [calculate_final_payment](#calculate_final_payment)                         | Calculate the final payment due to the contractor when ending the contract.                                                                                                                                          |
| [post_contract_estimate](#post_contract_estimate)                           | First payment is calculated from the number of working/calendar days between their start date and the start of the payment cycle.                                                                                    |
| [get_contract_templates](#get_contract_templates)                           | Retrieve a list of contract templates in your organization.                                                                                                                                                          |
| [get_worker_documents_by_id](#get_worker_documents_by_id)                   | Retrieve a list of documents of a worker.                                                                                                                                                                            |
| [get_download_worker_documents_by_id](#get_download_worker_documents_by_id) | Get the download link of worker document.                                                                                                                                                                            |

#### **get_contract_list**

Retrieve a list of contracts.

- HTTP Method: `GET`
- Endpoint: `/contracts`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| after_cursor | str | ❌ | Retrieve a list of contracts. |
| limit | float | ❌ | Retrieve a list of contracts. |
| order_direction | SortDirEnum | ❌ | Retrieve a list of contracts. |
| types | List[ContractTypeEnum] | ❌ | Retrieve a list of contracts. |
| statuses | List[ContractStatusEnum] | ❌ | Retrieve a list of contracts. |
| team_id | str | ❌ | Retrieve a list of contracts. |
| external_id | str | ❌ | Retrieve a list of contracts. |
| countries | List[str] | ❌ | Retrieve a list of contracts. |
| currencies | GetContractListCurrencies | ❌ | Retrieve a list of contracts. |
| search | str | ❌ | Retrieve a list of contracts. |
| sort_by | ContractsSortByEnum | ❌ | Retrieve a list of contracts. |

**Return Type**

`ContractListContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import SortDirEnum, GetContractListCurrencies, ContractsSortByEnum

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
types=[
    "ongoing_time_based"
]
statuses=[
    "new"
]
countries=[
    "US"
]
currencies=GetContractListCurrencies(**[
    "GBP"
])

result = sdk.contracts.get_contract_list(
    after_cursor="after_cursor",
    limit=10,
    order_direction="asc",
    types=types,
    statuses=statuses,
    team_id="team_id",
    external_id="external_id",
    countries=countries,
    currencies=currencies,
    search="search",
    sort_by="contract_title"
)

print(result)
```

#### **get_contract_by_id**

Retrieve a single contract.

- HTTP Method: `GET`
- Endpoint: `/contracts/{contract_id}`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| contract_id | str | ✅ | Retrieve a single contract. |

**Return Type**

`ContractContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.contracts.get_contract_by_id(contract_id="contract_id")

print(result)
```

#### **attach_external_id**

Add an external Id to a Deel contract. You can use this to add a Deel contract's refernece Id in your platform. External Id can be passed as a query parameter in List contract endpoint to find this conract later.

- HTTP Method: `PATCH`
- Endpoint: `/contracts/{contract_id}`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | InputToPatchContractExternalId | ✅ | The request body. |
| contract_id | str | ✅ | Add an external Id to a Deel contract. You can use this to add a Deel contract's refernece Id in your platform. External Id can be passed as a query parameter in List contract endpoint to find this conract later. |

**Return Type**

`GenericResultCreated`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import InputToPatchContractExternalId

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = InputToPatchContractExternalId(**{
    "data": {
        "external_id": "external_id"
    }
})

result = sdk.contracts.attach_external_id(
    request_body=request_body,
    contract_id="contract_id"
)

print(result)
```

#### **add_contract_document**

Attach a file to contract document.

- HTTP Method: `POST`
- Endpoint: `/contracts/{contract_id}/documents`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | dict | ❌ | The request body. |
| contract_id | str | ✅ | Attach a file to contract document. |

**Return Type**

`ContractDocumentContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import FileObject

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = {
    "file": "file"
}

result = sdk.contracts.add_contract_document(
    request_body=request_body,
    contract_id="contract_id"
)

print(result)
```

#### **edit_contract_document**

Overwrite the file currently attached to contract document.

- HTTP Method: `PUT`
- Endpoint: `/contracts/{contract_id}/documents`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | dict | ❌ | The request body. |
| contract_id | str | ✅ | Overwrite the file currently attached to contract document. |

**Return Type**

`ContractDocumentContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import FileObject

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = {
    "file": "file"
}

result = sdk.contracts.edit_contract_document(
    request_body=request_body,
    contract_id="contract_id"
)

print(result)
```

#### **get_alternate_emails_by_contract_id**

Returns an array of alternate email objects

- HTTP Method: `GET`
- Endpoint: `/contracts/{contract_id}/alternate_emails`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| contract_id | str | ✅ | Returns an array of alternate email objects |

**Return Type**

`List[AlternateEmailItem]`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.contracts.get_alternate_emails_by_contract_id(contract_id="contract_id")

print(result)
```

#### **sign_contract**

Sign a contract as a client.

- HTTP Method: `POST`
- Endpoint: `/contracts/{contract_id}/signatures`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | ContractSignatureToCreateContainer | ✅ | The request body. |
| contract_id | str | ✅ | Sign a contract as a client. |

**Return Type**

`GenericResultCreated`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import ContractSignatureToCreateContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = ContractSignatureToCreateContainer(**{
    "data": {
        "client_signature": "ea exercitat",
        "contract_template_id": 8.35
    }
})

result = sdk.contracts.sign_contract(
    request_body=request_body,
    contract_id="contract_id"
)

print(result)
```

#### **invite_to_sign_contract**

Invite a worker to sign the contract. Worker will be notified via email.

- HTTP Method: `POST`
- Endpoint: `/contracts/{contract_id}/invitations`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | ContractInvitationToCreateContainer | ✅ | The request body. |
| contract_id | str | ✅ | Invite a worker to sign the contract. Worker will be notified via email. |

**Return Type**

`GenericResultCreated`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import ContractInvitationToCreateContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = ContractInvitationToCreateContainer(**{
    "data": {
        "email": "eiusm",
        "message": "officia ut"
    }
})

result = sdk.contracts.invite_to_sign_contract(
    request_body=request_body,
    contract_id="contract_id"
)

print(result)
```

#### **uninvite_to_sign_contract**

Remove invite in order to re-invite a worker to sign the contract.

- HTTP Method: `DELETE`
- Endpoint: `/contracts/{contract_id}/invitations`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| contract_id | str | ✅ | Remove invite in order to re-invite a worker to sign the contract. |

**Return Type**

`GenericResultDeleted`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.contracts.uninvite_to_sign_contract(contract_id="contract_id")

print(result)
```

#### **calculate_final_payment**

Calculate the final payment due to the contractor when ending the contract.

- HTTP Method: `GET`
- Endpoint: `/contracts/{contract_id}/final-payments`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| contract_id | str | ✅ | Calculate the final payment due to the contractor when ending the contract. |
| end_date | str | ❌ | Calculate the final payment due to the contractor when ending the contract. |
| calculation_type | CalculateFinalPaymentCalculationType | ❌ | Calculate the final payment due to the contractor when ending the contract. |
| workweek_start | str | ❌ | Calculate the final payment due to the contractor when ending the contract. |
| workweek_end | str | ❌ | Calculate the final payment due to the contractor when ending the contract. |

**Return Type**

`FinalPaymentCalculatedContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import CalculateFinalPaymentCalculationType

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.contracts.calculate_final_payment(
    contract_id="contract_id",
    end_date="1999-12-31",
    calculation_type="CUSTOM_AMOUNT",
    workweek_start="workweek_start",
    workweek_end="workweek_end"
)

print(result)
```

#### **post_contract_estimate**

First payment is calculated from the number of working/calendar days between their start date and the start of the payment cycle.

- HTTP Method: `POST`
- Endpoint: `/contracts/estimate`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | EstimateFirstPaymentContainer | ✅ | The request body. |

**Return Type**

`ResponseEstimateFirstPaymentContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import EstimateFirstPaymentContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = EstimateFirstPaymentContainer(**{
    "data": {
        "type_": "ongoing_time_based",
        "country_code": "US",
        "start_date": "1999-12-31",
        "compensation_details": {
            "amount": 2500,
            "currency_code": "GBP",
            "scale": "weekly",
            "cycle_end": 30.28,
            "cycle_end_type": "DAY_OF_WEEK",
            "payment_due_type": "REGULAR",
            "payment_due_days": 11.81,
            "calculation_type": "CUSTOM_AMOUNT",
            "work_week_start": "Sunday",
            "work_week_end": "Sunday"
        }
    }
})

result = sdk.contracts.post_contract_estimate(request_body=request_body)

print(result)
```

#### **get_contract_templates**

Retrieve a list of contract templates in your organization.

- HTTP Method: `GET`
- Endpoint: `/contract-templates`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|

**Return Type**

`ContractTemplateListContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.contracts.get_contract_templates()

print(result)
```

#### **get_worker_documents_by_id**

Retrieve a list of documents of a worker.

- HTTP Method: `GET`
- Endpoint: `/workers/{worker_id}/documents`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| worker_id | str | ✅ | Retrieve a list of documents of a worker. |

**Return Type**

`WorkerDocumentsByIdContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.contracts.get_worker_documents_by_id(worker_id="worker_id")

print(result)
```

#### **get_download_worker_documents_by_id**

Get the download link of worker document.

- HTTP Method: `GET`
- Endpoint: `/workers/{worker_id}/documents/{document_id}/download`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| worker_id | str | ✅ | Get the download link of worker document. |
| document_id | float | ✅ | Get the download link of worker document. |

**Return Type**

`DownloadWorkerDocumentsByIdContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.contracts.get_download_worker_documents_by_id(
    worker_id="worker_id",
    document_id=8.43
)

print(result)
```

### TasksService

A list of all methods in the `TasksService` service. Click on the method name to view detailed information about that method.

| Methods                                               | Description                                                     |
| :---------------------------------------------------- | :-------------------------------------------------------------- |
| [get_tasks_by_contract](#get_tasks_by_contract)       | Retrieve a list of tasks for a given contract.                  |
| [create_contract_pgo_tak](#create_contract_pgo_tak)   | Create a new task for the contractor.                           |
| [create_task_many_review](#create_task_many_review)   | Review multiple tasks to approve or decline the submitted work. |
| [create_task_review_by_id](#create_task_review_by_id) | Review a single task to approve or decline the submitted work.  |
| [delete_contract_pgo_tak](#delete_contract_pgo_tak)   | Delete task from the contract.                                  |

#### **get_tasks_by_contract**

Retrieve a list of tasks for a given contract.

- HTTP Method: `GET`
- Endpoint: `/contracts/{contract_id}/tasks`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| contract_id | str | ✅ | Retrieve a list of tasks for a given contract. |

**Return Type**

`TaskListContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.tasks.get_tasks_by_contract(contract_id="contract_id")

print(result)
```

#### **create_contract_pgo_tak**

Create a new task for the contractor.

- HTTP Method: `POST`
- Endpoint: `/contracts/{contract_id}/tasks`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | InputToCreatePgoTask | ✅ | The request body. |
| contract_id | str | ✅ | Create a new task for the contractor. |

**Return Type**

`TaskCreatedContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import InputToCreatePgoTask

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = InputToCreatePgoTask(**{
    "data": {
        "amount": "123.45",
        "date_submitted": "1999-12-31",
        "description": "Make the button pop.",
        "attachment": {
            "filename": "filename",
            "key": "key"
        }
    }
})

result = sdk.tasks.create_contract_pgo_tak(
    request_body=request_body,
    contract_id="contract_id"
)

print(result)
```

#### **create_task_many_review**

Review multiple tasks to approve or decline the submitted work.

- HTTP Method: `POST`
- Endpoint: `/contracts/{contract_id}/tasks/many/reviews`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | RequestBodyToCreatePgoTaskReviewsReviewsContainer | ❌ | The request body. |
| contract_id | str | ✅ | Review multiple tasks to approve or decline the submitted work. |

**Return Type**

`TaskListContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import RequestBodyToCreatePgoTaskReviewsReviewsContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = RequestBodyToCreatePgoTaskReviewsReviewsContainer(**{
    "data": {
        "status": "approved",
        "reason": "Great work.",
        "ids": [
            "00000000-0000-0000-0000-000000000000"
        ]
    }
})

result = sdk.tasks.create_task_many_review(
    request_body=request_body,
    contract_id="contract_id"
)

print(result)
```

#### **create_task_review_by_id**

Review a single task to approve or decline the submitted work.

- HTTP Method: `POST`
- Endpoint: `/contracts/{contract_id}/tasks/{task_id}/reviews`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | RequestBodyToCreatePgoTaskReviewsByIdReviewsContainer | ❌ | The request body. |
| contract_id | str | ✅ | Review a single task to approve or decline the submitted work. |
| task_id | str | ✅ | Review a single task to approve or decline the submitted work. |

**Return Type**

`TaskListContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import RequestBodyToCreatePgoTaskReviewsByIdReviewsContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = RequestBodyToCreatePgoTaskReviewsByIdReviewsContainer(**{
    "data": {
        "status": "approved",
        "reason": "Excited!"
    }
})

result = sdk.tasks.create_task_review_by_id(
    request_body=request_body,
    contract_id="contract_id",
    task_id="task_id"
)

print(result)
```

#### **delete_contract_pgo_tak**

Delete task from the contract.

- HTTP Method: `DELETE`
- Endpoint: `/contracts/{contract_id}/tasks/{task_id}`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| contract_id | str | ✅ | Delete task from the contract. |
| task_id | str | ✅ | Delete task from the contract. |
| reason | str | ❌ | Delete task from the contract. |

**Return Type**

`GenericResultDeleted`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.tasks.delete_contract_pgo_tak(
    contract_id="contract_id",
    task_id="task_id",
    reason="reason"
)

print(result)
```

### TimesheetsService

A list of all methods in the `TimesheetsService` service. Click on the method name to view detailed information about that method.

| Methods                                                   | Description                                                                                                                                        |
| :-------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------- |
| [get_timesheets_by_contract](#get_timesheets_by_contract) | Retrieve a list of timesheets found for a contract.                                                                                                |
| [get_timesheets](#get_timesheets)                         | Retrieve a list of timesheets in your Deel account. You can filter the list by providing additional paramters e.g. contract_id, contract_type etc. |
| [create_timesheet](#create_timesheet)                     | Submit work for a contractor.                                                                                                                      |
| [get_timesheet_by_id](#get_timesheet_by_id)               | Retrieve a single timesheet entry by Id.                                                                                                           |
| [update_timesheet_by_id](#update_timesheet_by_id)         | Update a single timesheet entry.                                                                                                                   |
| [delete_timesheet_by_id](#delete_timesheet_by_id)         | Delete a single timesheet entry.                                                                                                                   |
| [create_timesheet_review](#create_timesheet_review)       | Review a timesheet to approve or decline submitted work.                                                                                           |
| [create_timesheet_reviews](#create_timesheet_reviews)     | Review a batch of timesheets to approve or reject submitted work.                                                                                  |

#### **get_timesheets_by_contract**

Retrieve a list of timesheets found for a contract.

- HTTP Method: `GET`
- Endpoint: `/contracts/{contract_id}/timesheets`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| contract_id | str | ✅ | Retrieve a list of timesheets found for a contract. |
| contract_types | List[ContractTypeEnum] | ❌ | Retrieve a list of timesheets found for a contract. |
| statuses | List[TimesheetStatusEnum] | ❌ | Retrieve a list of timesheets found for a contract. |
| reporter_id | str | ❌ | Retrieve a list of timesheets found for a contract. |
| date_from | str | ❌ | Retrieve a list of timesheets found for a contract. |
| date_to | str | ❌ | Retrieve a list of timesheets found for a contract. |
| limit | float | ❌ | Retrieve a list of timesheets found for a contract. |
| offset | float | ❌ | Retrieve a list of timesheets found for a contract. |

**Return Type**

`TimesheetListContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
contract_types=[
    "ongoing_time_based"
]
statuses=[
    "approved"
]

result = sdk.timesheets.get_timesheets_by_contract(
    contract_id="contract_id",
    contract_types=contract_types,
    statuses=statuses,
    reporter_id="reporter_id",
    date_from="1999-12-31",
    date_to="1999-12-31",
    limit=99,
    offset=564786626.18
)

print(result)
```

#### **get_timesheets**

Retrieve a list of timesheets in your Deel account. You can filter the list by providing additional paramters e.g. contract_id, contract_type etc.

- HTTP Method: `GET`
- Endpoint: `/timesheets`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| contract_id | str | ❌ | Retrieve a list of timesheets in your Deel account. You can filter the list by providing additional paramters e.g. contract_id, contract_type etc. |
| contract_types | List[ContractTypeEnum] | ❌ | Retrieve a list of timesheets in your Deel account. You can filter the list by providing additional paramters e.g. contract_id, contract_type etc. |
| statuses | List[TimesheetStatusEnum] | ❌ | Retrieve a list of timesheets in your Deel account. You can filter the list by providing additional paramters e.g. contract_id, contract_type etc. |
| reporter_id | str | ❌ | Retrieve a list of timesheets in your Deel account. You can filter the list by providing additional paramters e.g. contract_id, contract_type etc. |
| date_from | str | ❌ | Retrieve a list of timesheets in your Deel account. You can filter the list by providing additional paramters e.g. contract_id, contract_type etc. |
| date_to | str | ❌ | Retrieve a list of timesheets in your Deel account. You can filter the list by providing additional paramters e.g. contract_id, contract_type etc. |
| limit | float | ❌ | Retrieve a list of timesheets in your Deel account. You can filter the list by providing additional paramters e.g. contract_id, contract_type etc. |
| offset | float | ❌ | Retrieve a list of timesheets in your Deel account. You can filter the list by providing additional paramters e.g. contract_id, contract_type etc. |

**Return Type**

`TimesheetListContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
contract_types=[
    "ongoing_time_based"
]
statuses=[
    "approved"
]

result = sdk.timesheets.get_timesheets(
    contract_id="contract_id",
    contract_types=contract_types,
    statuses=statuses,
    reporter_id="reporter_id",
    date_from="1999-12-31",
    date_to="1999-12-31",
    limit=99,
    offset=911169937.96
)

print(result)
```

#### **create_timesheet**

Submit work for a contractor.

- HTTP Method: `POST`
- Endpoint: `/timesheets`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | TimesheetToCreateContainer | ✅ | The request body. |

**Return Type**

`InvoiceAdjustmentCreatedContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import TimesheetToCreateContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = TimesheetToCreateContainer(**{
    "data": {
        "contract_id": "contract_id",
        "description": "description",
        "date_submitted": "1999-12-31",
        "quantity": 2
    }
})

result = sdk.timesheets.create_timesheet(request_body=request_body)

print(result)
```

#### **get_timesheet_by_id**

Retrieve a single timesheet entry by Id.

- HTTP Method: `GET`
- Endpoint: `/timesheets/{timesheet_id}`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| timesheet_id | str | ✅ | Retrieve a single timesheet entry by Id. |

**Return Type**

`TimesheetContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.timesheets.get_timesheet_by_id(timesheet_id="timesheet_id")

print(result)
```

#### **update_timesheet_by_id**

Update a single timesheet entry.

- HTTP Method: `PATCH`
- Endpoint: `/timesheets/{timesheet_id}`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | TimesheetToUpdateContainer | ✅ | The request body. |
| timesheet_id | str | ✅ | Update a single timesheet entry. |

**Return Type**

`GenericResultUpdated`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import TimesheetToUpdateContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = TimesheetToUpdateContainer(**{
    "data": {
        "description": "description",
        "quantity": 3.77
    }
})

result = sdk.timesheets.update_timesheet_by_id(
    request_body=request_body,
    timesheet_id="timesheet_id"
)

print(result)
```

#### **delete_timesheet_by_id**

Delete a single timesheet entry.

- HTTP Method: `DELETE`
- Endpoint: `/timesheets/{timesheet_id}`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| timesheet_id | str | ✅ | Delete a single timesheet entry. |
| reason | str | ❌ | Delete a single timesheet entry. |

**Return Type**

`GenericResultDeleted`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.timesheets.delete_timesheet_by_id(
    timesheet_id="timesheet_id",
    reason="reason"
)

print(result)
```

#### **create_timesheet_review**

Review a timesheet to approve or decline submitted work.

- HTTP Method: `POST`
- Endpoint: `/timesheets/{timesheet_id}/reviews`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | TimesheetReviewToCreateContainer | ❌ | The request body. |
| timesheet_id | str | ✅ | Review a timesheet to approve or decline submitted work. |

**Return Type**

`GenericResultCreated`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import TimesheetReviewToCreateContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = TimesheetReviewToCreateContainer(**{
    "data": {
        "status": "approved",
        "reason": "reason"
    }
})

result = sdk.timesheets.create_timesheet_review(
    request_body=request_body,
    timesheet_id="timesheet_id"
)

print(result)
```

#### **create_timesheet_reviews**

Review a batch of timesheets to approve or reject submitted work.

- HTTP Method: `POST`
- Endpoint: `/timesheets/many/reviews`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | TimesheetReviewsToCreateContainer | ❌ | The request body. |

**Return Type**

`GenericResultCreated`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import TimesheetReviewsToCreateContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = TimesheetReviewsToCreateContainer(**{
    "data": {
        "status": "approved",
        "reason": "reason",
        "ids": [
            1.77
        ]
    }
})

result = sdk.timesheets.create_timesheet_reviews(request_body=request_body)

print(result)
```

### MilestonesService

A list of all methods in the `MilestonesService` service. Click on the method name to view detailed information about that method.

| Methods                                                                 | Description                                                       |
| :---------------------------------------------------------------------- | :---------------------------------------------------------------- |
| [get_milestones_by_contract](#get_milestones_by_contract)               | Retrieve a list of milestones found for a contract.               |
| [create_milestone](#create_milestone)                                   | Add a new milestone to contract.                                  |
| [get_milestones_by_contract_and_id](#get_milestones_by_contract_and_id) | Retrieve a single milestone.                                      |
| [delete_milestone_by_id](#delete_milestone_by_id)                       | Delete a single milestone from a contract.                        |
| [create_milestone_review](#create_milestone_review)                     | Review a milestone to approve or decline submitted work.          |
| [create_milestone_reviews](#create_milestone_reviews)                   | Review a batch of milestones to approve or reject submitted work. |

#### **get_milestones_by_contract**

Retrieve a list of milestones found for a contract.

- HTTP Method: `GET`
- Endpoint: `/contracts/{contract_id}/milestones`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| contract_id | str | ✅ | Retrieve a list of milestones found for a contract. |

**Return Type**

`MilestoneListContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.milestones.get_milestones_by_contract(contract_id="contract_id")

print(result)
```

#### **create_milestone**

Add a new milestone to contract.

- HTTP Method: `POST`
- Endpoint: `/contracts/{contract_id}/milestones`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | MilestoneToCreateContainer | ❌ | The request body. |
| contract_id | str | ✅ | Add a new milestone to contract. |

**Return Type**

`GenericResultCreated`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import MilestoneToCreateContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = MilestoneToCreateContainer(**{
    "data": {
        "amount": "900.00",
        "title": "Sprint 2",
        "description": "Sprint #2"
    }
})

result = sdk.milestones.create_milestone(
    request_body=request_body,
    contract_id="contract_id"
)

print(result)
```

#### **get_milestones_by_contract_and_id**

Retrieve a single milestone.

- HTTP Method: `GET`
- Endpoint: `/contracts/{contract_id}/milestones/{milestone_id}`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| contract_id | str | ✅ | Retrieve a single milestone. |
| milestone_id | str | ✅ | Retrieve a single milestone. |

**Return Type**

`MilestoneContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.milestones.get_milestones_by_contract_and_id(
    contract_id="contract_id",
    milestone_id="milestone_id"
)

print(result)
```

#### **delete_milestone_by_id**

Delete a single milestone from a contract.

- HTTP Method: `DELETE`
- Endpoint: `/contracts/{contract_id}/milestones/{milestone_id}`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| contract_id | str | ✅ | Delete a single milestone from a contract. |
| milestone_id | str | ✅ | Delete a single milestone from a contract. |

**Return Type**

`GenericResultDeleted`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.milestones.delete_milestone_by_id(
    contract_id="contract_id",
    milestone_id="milestone_id"
)

print(result)
```

#### **create_milestone_review**

Review a milestone to approve or decline submitted work.

- HTTP Method: `POST`
- Endpoint: `/contracts/{contract_id}/milestones/{milestone_id}/reviews`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | MilestoneReviewToCreateContainer | ❌ | The request body. |
| contract_id | str | ✅ | Review a milestone to approve or decline submitted work. |
| milestone_id | str | ✅ | Review a milestone to approve or decline submitted work. |

**Return Type**

`GenericResultCreated`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import MilestoneReviewToCreateContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = MilestoneReviewToCreateContainer(**{
    "data": {
        "status": "approved",
        "reason": "reason"
    }
})

result = sdk.milestones.create_milestone_review(
    request_body=request_body,
    contract_id="contract_id",
    milestone_id="milestone_id"
)

print(result)
```

#### **create_milestone_reviews**

Review a batch of milestones to approve or reject submitted work.

- HTTP Method: `POST`
- Endpoint: `/contracts/{contract_id}/milestones/many/reviews`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | MilestoneReviewsToCreateContainer | ❌ | The request body. |
| contract_id | str | ✅ | Review a batch of milestones to approve or reject submitted work. |

**Return Type**

`GenericResultCreated`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import MilestoneReviewsToCreateContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = MilestoneReviewsToCreateContainer(**{
    "data": {
        "status": "approved",
        "reason": "reason",
        "ids": [
            6.78
        ]
    }
})

result = sdk.milestones.create_milestone_reviews(
    request_body=request_body,
    contract_id="contract_id"
)

print(result)
```

### OffCyclePaymentsService

A list of all methods in the `OffCyclePaymentsService` service. Click on the method name to view detailed information about that method.

| Methods                                                                               | Description                                                                            |
| :------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------- |
| [get_off_cycle_payments_by_contract](#get_off_cycle_payments_by_contract)             | Retrieve a list of off-cycle payments for the given contract id.                       |
| [create_off_cycle_payment](#create_off_cycle_payment)                                 | Add a new invoice line-item for the purpose of off-cycle payment for a given contract. |
| [get_off_cycle_payment_by_contract_and_id](#get_off_cycle_payment_by_contract_and_id) | Retrieve a single off-cycle payment.                                                   |

#### **get_off_cycle_payments_by_contract**

Retrieve a list of off-cycle payments for the given contract id.

- HTTP Method: `GET`
- Endpoint: `/contracts/{contract_id}/off-cycle-payments`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| contract_id | str | ✅ | Retrieve a list of off-cycle payments for the given contract id. |

**Return Type**

`OffCyclePaymentListContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.off_cycle_payments.get_off_cycle_payments_by_contract(contract_id="contract_id")

print(result)
```

#### **create_off_cycle_payment**

Add a new invoice line-item for the purpose of off-cycle payment for a given contract.

- HTTP Method: `POST`
- Endpoint: `/contracts/{contract_id}/off-cycle-payments`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | OffCyclePaymentToCreateContainer | ❌ | The request body. |
| contract_id | str | ✅ | Add a new invoice line-item for the purpose of off-cycle payment for a given contract. |

**Return Type**

`GenericResultCreatedWithId`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import OffCyclePaymentToCreateContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = OffCyclePaymentToCreateContainer(**{
    "data": {
        "date_submitted": "1999-12-31",
        "amount": 2500,
        "description": "description"
    }
})

result = sdk.off_cycle_payments.create_off_cycle_payment(
    request_body=request_body,
    contract_id="contract_id"
)

print(result)
```

#### **get_off_cycle_payment_by_contract_and_id**

Retrieve a single off-cycle payment.

- HTTP Method: `GET`
- Endpoint: `/contracts/{contract_id}/off-cycle-payments/{offcycle_payment_id}`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| contract_id | str | ✅ | Retrieve a single off-cycle payment. |
| offcycle_payment_id | str | ✅ | Retrieve a single off-cycle payment. |

**Return Type**

`OffCyclePaymentContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.off_cycle_payments.get_off_cycle_payment_by_contract_and_id(
    contract_id="contract_id",
    offcycle_payment_id="offcycle_payment_id"
)

print(result)
```

### TimeOffService

A list of all methods in the `TimeOffService` service. Click on the method name to view detailed information about that method.

| Methods                                               | Description                                                        |
| :---------------------------------------------------- | :----------------------------------------------------------------- |
| [get_eor_time_offs](#get_eor_time_offs)               | Retrieve the list of time off requests by an employee.             |
| [create_eor_time_offs](#create_eor_time_offs)         | Add a time off request for a full-time employee.                   |
| [edit_eor_time_offs](#edit_eor_time_offs)             | Edit a time off request for a full-time employee.                  |
| [delete_eor_time_offs](#delete_eor_time_offs)         | Cancel a time off request for an employee.                         |
| [get_eor_entitlements](#get_eor_entitlements)         | Retrieve a list of time off entitlements for a full-time employee. |
| [get_eor_client_time_offs](#get_eor_client_time_offs) | List of time offs for all employees in your organization.          |
| [review_timeoff](#review_timeoff)                     | Approve or decline an employee's time off request.                 |

#### **get_eor_time_offs**

Retrieve the list of time off requests by an employee.

- HTTP Method: `GET`
- Endpoint: `/contracts/{contract_id}/time-offs`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| contract_id | str | ✅ | Retrieve the list of time off requests by an employee. |

**Return Type**

`EorTimeoffsContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.time_off.get_eor_time_offs(contract_id="contract_id")

print(result)
```

#### **create_eor_time_offs**

Add a time off request for a full-time employee.

- HTTP Method: `POST`
- Endpoint: `/contracts/{contract_id}/time-offs`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | CreateTimeoffContainer | ❌ | The request body. |
| contract_id | str | ✅ | Add a time off request for a full-time employee. |

**Return Type**

`EorTimeoffsItemContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import CreateTimeoffContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CreateTimeoffContainer(**{
    "data": {
        "type_": "VACATION",
        "start_date": "2022-09-03T00:00:00.000Z",
        "end_date": "2022-09-05T00:00:00.000Z",
        "with_multiple_dates": True,
        "reason": "Holiday",
        "is_start_date_half_day": True,
        "is_end_date_half_day": False,
        "other_timeoff_name": "Birthday"
    }
})

result = sdk.time_off.create_eor_time_offs(
    request_body=request_body,
    contract_id="contract_id"
)

print(result)
```

#### **edit_eor_time_offs**

Edit a time off request for a full-time employee.

- HTTP Method: `PUT`
- Endpoint: `/contracts/{contract_id}/time-offs/{timeoff_id}`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | CreateTimeoffContainer | ❌ | The request body. |
| contract_id | str | ✅ | Edit a time off request for a full-time employee. |
| timeoff_id | str | ✅ | Edit a time off request for a full-time employee. |

**Return Type**

`EorTimeoffsItemContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import CreateTimeoffContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CreateTimeoffContainer(**{
    "data": {
        "type_": "VACATION",
        "start_date": "2022-09-03T00:00:00.000Z",
        "end_date": "2022-09-05T00:00:00.000Z",
        "with_multiple_dates": True,
        "reason": "Holiday",
        "is_start_date_half_day": True,
        "is_end_date_half_day": False,
        "other_timeoff_name": "Birthday"
    }
})

result = sdk.time_off.edit_eor_time_offs(
    request_body=request_body,
    contract_id="contract_id",
    timeoff_id="timeoff_id"
)

print(result)
```

#### **delete_eor_time_offs**

Cancel a time off request for an employee.

- HTTP Method: `DELETE`
- Endpoint: `/contracts/{contract_id}/time-offs/{timeoff_id}`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| contract_id | str | ✅ | Cancel a time off request for an employee. |
| timeoff_id | str | ✅ | Cancel a time off request for an employee. |

**Return Type**

`GenericResultDeleted`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.time_off.delete_eor_time_offs(
    contract_id="contract_id",
    timeoff_id="timeoff_id"
)

print(result)
```

#### **get_eor_entitlements**

Retrieve a list of time off entitlements for a full-time employee.

- HTTP Method: `GET`
- Endpoint: `/contracts/{contract_id}/entitlements`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| contract_id | str | ✅ | Retrieve a list of time off entitlements for a full-time employee. |

**Return Type**

`EorEntitlementsContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.time_off.get_eor_entitlements(contract_id="contract_id")

print(result)
```

#### **get_eor_client_time_offs**

List of time offs for all employees in your organization.

- HTTP Method: `GET`
- Endpoint: `/time-offs`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|

**Return Type**

`EorClientTimeoffsContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.time_off.get_eor_client_time_offs()

print(result)
```

#### **review_timeoff**

Approve or decline an employee's time off request.

- HTTP Method: `PATCH`
- Endpoint: `/time-offs/{timeoff_id}/review`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | TimeoffToReviewContainer | ✅ | The request body. |
| timeoff_id | str | ✅ | Approve or decline an employee's time off request. |

**Return Type**

`GenericResultUpdated`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import TimeoffToReviewContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = TimeoffToReviewContainer(**{
    "data": {
        "is_approved": True,
        "denial_reason": "Not allowed for this day."
    }
})

result = sdk.time_off.review_timeoff(
    request_body=request_body,
    timeoff_id="timeoff_id"
)

print(result)
```

### InvoicesService

A list of all methods in the `InvoicesService` service. Click on the method name to view detailed information about that method.

| Methods                                                                           | Description                                                                                                                                                   |
| :-------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [get_invoice_adjustments_by_contract_id](#get_invoice_adjustments_by_contract_id) | Retrieve invoice line items for a given contract id.                                                                                                          |
| [get_invoice_adjustments](#get_invoice_adjustments)                               | Retrieve invoice adjustments. You can filter the list by providing additional parameters e.g. contract_id, contract_type etc.                                 |
| [create_invoice_adjustment](#create_invoice_adjustment)                           | Create an invoice adjustment using this endpoint. For example, you can add a bonus, commission, VAT %, deduction etc. to an invoice.                          |
| [update_invoice_adjustment_by_id](#update_invoice_adjustment_by_id)               | Update an existing invoice adjustment. It is not possible to update VAT adjustments, we recommend you to delete the existing VAT adjust and create a new one. |
| [delete_invoice_adjustment_by_id](#delete_invoice_adjustment_by_id)               | Delete an existing invoice adjustment.                                                                                                                        |
| [create_invoice_adjustment_review](#create_invoice_adjustment_review)             | Review an invoice adjustment to approve or decline it.                                                                                                        |
| [create_invoice_adjustment_reviews](#create_invoice_adjustment_reviews)           | Review multiple invoice adjustments to approve or decline a batch.                                                                                            |
| [get_invoice_adjustments_attachment](#get_invoice_adjustments_attachment)         | Retrieve Attachment file url of specified id.                                                                                                                 |

#### **get_invoice_adjustments_by_contract_id**

Retrieve invoice line items for a given contract id.

- HTTP Method: `GET`
- Endpoint: `/contracts/{contract_id}/invoice-adjustments`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| contract_id | str | ✅ | Retrieve invoice line items for a given contract id. |
| contract_types | List[ContractTypeEnum] | ❌ | Retrieve invoice line items for a given contract id. |
| types | List[InvoiceAdjustmentTypeEnum] | ❌ | Retrieve invoice line items for a given contract id. |
| statuses | List[InvoiceAdjustmentStatusEnum] | ❌ | Retrieve invoice line items for a given contract id. |
| invoice_id | str | ❌ | Retrieve invoice line items for a given contract id. |
| reporter_id | str | ❌ | Retrieve invoice line items for a given contract id. |
| date_from | str | ❌ | Retrieve invoice line items for a given contract id. |
| date_to | str | ❌ | Retrieve invoice line items for a given contract id. |
| limit | float | ❌ | Retrieve invoice line items for a given contract id. |
| offset | float | ❌ | Retrieve invoice line items for a given contract id. |

**Return Type**

`InvoiceAdjustmentListContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
contract_types=[
    "ongoing_time_based"
]
types=[
    "accrued_holiday"
]
statuses=[
    "approved"
]

result = sdk.invoices.get_invoice_adjustments_by_contract_id(
    contract_id="contract_id",
    contract_types=contract_types,
    types=types,
    statuses=statuses,
    invoice_id="invoice_id",
    reporter_id="reporter_id",
    date_from="1999-12-31",
    date_to="1999-12-31",
    limit=10,
    offset=226515477.25
)

print(result)
```

#### **get_invoice_adjustments**

Retrieve invoice adjustments. You can filter the list by providing additional parameters e.g. contract_id, contract_type etc.

- HTTP Method: `GET`
- Endpoint: `/invoice-adjustments`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| contract_id | str | ❌ | Retrieve invoice adjustments. You can filter the list by providing additional parameters e.g. contract_id, contract_type etc. |
| contract_types | List[ContractTypeEnum] | ❌ | Retrieve invoice adjustments. You can filter the list by providing additional parameters e.g. contract_id, contract_type etc. |
| types | List[InvoiceAdjustmentTypeEnum] | ❌ | Retrieve invoice adjustments. You can filter the list by providing additional parameters e.g. contract_id, contract_type etc. |
| statuses | List[InvoiceAdjustmentStatusEnum] | ❌ | Retrieve invoice adjustments. You can filter the list by providing additional parameters e.g. contract_id, contract_type etc. |
| invoice_id | str | ❌ | Retrieve invoice adjustments. You can filter the list by providing additional parameters e.g. contract_id, contract_type etc. |
| reporter_id | str | ❌ | Retrieve invoice adjustments. You can filter the list by providing additional parameters e.g. contract_id, contract_type etc. |
| date_from | str | ❌ | Retrieve invoice adjustments. You can filter the list by providing additional parameters e.g. contract_id, contract_type etc. |
| date_to | str | ❌ | Retrieve invoice adjustments. You can filter the list by providing additional parameters e.g. contract_id, contract_type etc. |
| limit | float | ❌ | Retrieve invoice adjustments. You can filter the list by providing additional parameters e.g. contract_id, contract_type etc. |
| offset | float | ❌ | Retrieve invoice adjustments. You can filter the list by providing additional parameters e.g. contract_id, contract_type etc. |

**Return Type**

`InvoiceAdjustmentListContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
contract_types=[
    "ongoing_time_based"
]
types=[
    "accrued_holiday"
]
statuses=[
    "approved"
]

result = sdk.invoices.get_invoice_adjustments(
    contract_id="contract_id",
    contract_types=contract_types,
    types=types,
    statuses=statuses,
    invoice_id="invoice_id",
    reporter_id="reporter_id",
    date_from="1999-12-31",
    date_to="1999-12-31",
    limit=10,
    offset=240522187.51
)

print(result)
```

#### **create_invoice_adjustment**

Create an invoice adjustment using this endpoint. For example, you can add a bonus, commission, VAT %, deduction etc. to an invoice.

- HTTP Method: `POST`
- Endpoint: `/invoice-adjustments`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | InvoiceAdjustmentToCreateContainer | ✅ | The request body. |
| recurring | bool | ❌ | Create an invoice adjustment using this endpoint. For example, you can add a bonus, commission, VAT %, deduction etc. to an invoice. |

**Return Type**

`InvoiceAdjustmentCreatedContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import InvoiceAdjustmentToCreateContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = InvoiceAdjustmentToCreateContainer(**{
    "data": {
        "contract_id": "contract_id",
        "date_submitted": "1999-12-31",
        "type_": "bonus",
        "amount": 2500,
        "description": "Bonus for being awesome.",
        "payment_cycle_id": 6.69
    }
})

result = sdk.invoices.create_invoice_adjustment(
    request_body=request_body,
    recurring=False
)

print(result)
```

#### **update_invoice_adjustment_by_id**

Update an existing invoice adjustment. It is not possible to update VAT adjustments, we recommend you to delete the existing VAT adjust and create a new one.

- HTTP Method: `PATCH`
- Endpoint: `/invoice-adjustments/{invoice_adjustment_id}`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | InvoiceAdjustmentToUpdateContainer | ✅ | The request body. |
| invoice_adjustment_id | str | ✅ | Update an existing invoice adjustment. It is not possible to update VAT adjustments, we recommend you to delete the existing VAT adjust and create a new one. |

**Return Type**

`GenericResultUpdated`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import InvoiceAdjustmentToUpdateContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = InvoiceAdjustmentToUpdateContainer(**{
    "data": {
        "description": "sunt laborum Duis exercitation id",
        "amount": 9.39
    }
})

result = sdk.invoices.update_invoice_adjustment_by_id(
    request_body=request_body,
    invoice_adjustment_id="invoice_adjustment_id"
)

print(result)
```

#### **delete_invoice_adjustment_by_id**

Delete an existing invoice adjustment.

- HTTP Method: `DELETE`
- Endpoint: `/invoice-adjustments/{invoice_adjustment_id}`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| invoice_adjustment_id | str | ✅ | Delete an existing invoice adjustment. |
| reason | str | ❌ | Delete an existing invoice adjustment. |

**Return Type**

`GenericResultDeleted`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.invoices.delete_invoice_adjustment_by_id(
    invoice_adjustment_id="invoice_adjustment_id",
    reason="reason"
)

print(result)
```

#### **create_invoice_adjustment_review**

Review an invoice adjustment to approve or decline it.

- HTTP Method: `POST`
- Endpoint: `/invoice-adjustments/{invoice_adjustment_id}/reviews`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | InvoiceAdjustmentReviewToCreateContainer | ❌ | The request body. |
| invoice_adjustment_id | str | ✅ | Review an invoice adjustment to approve or decline it. |

**Return Type**

`GenericResultCreated`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import InvoiceAdjustmentReviewToCreateContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = InvoiceAdjustmentReviewToCreateContainer(**{
    "data": {
        "status": "approved",
        "reason": "reason"
    }
})

result = sdk.invoices.create_invoice_adjustment_review(
    request_body=request_body,
    invoice_adjustment_id="invoice_adjustment_id"
)

print(result)
```

#### **create_invoice_adjustment_reviews**

Review multiple invoice adjustments to approve or decline a batch.

- HTTP Method: `POST`
- Endpoint: `/invoice-adjustments/many/reviews`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | InvoiceAdjustmentReviewsToCreateContainer | ❌ | The request body. |

**Return Type**

`GenericResultCreated`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import InvoiceAdjustmentReviewsToCreateContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = InvoiceAdjustmentReviewsToCreateContainer(**{
    "data": {
        "status": "approved",
        "reason": "reason",
        "ids": [
            1.77
        ]
    }
})

result = sdk.invoices.create_invoice_adjustment_reviews(request_body=request_body)

print(result)
```

#### **get_invoice_adjustments_attachment**

Retrieve Attachment file url of specified id.

- HTTP Method: `GET`
- Endpoint: `/invoice-adjustments/{invoice_adjustment_id}/attachment`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| invoice_adjustment_id | str | ✅ | Retrieve Attachment file url of specified id. |

**Return Type**

`InvoiceAdjustmentAttachmentContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.invoices.get_invoice_adjustments_attachment(invoice_adjustment_id="invoice_adjustment_id")

print(result)
```

### OrganizationsService

A list of all methods in the `OrganizationsService` service. Click on the method name to view detailed information about that method.

| Methods                                         | Description                                                                                            |
| :---------------------------------------------- | :----------------------------------------------------------------------------------------------------- |
| [get_legal_entity_list](#get_legal_entity_list) | Retrieve a list of legal entities in your account.                                                     |
| [get_organizations](#get_organizations)         | Retrieve the current organization details. Organization is automatically detected from the auth token. |
| [get_teams](#get_teams)                         | Retrieve a list of teams in your organization.                                                         |
| [get_agreements](#get_agreements)               | This end-point returns a list of your agreements with Deel.                                            |
| [get_departments](#get_departments)             | Get list of organization departments.                                                                  |
| [get_working_locations](#get_working_locations) | Get organization working locations.                                                                    |

#### **get_legal_entity_list**

Retrieve a list of legal entities in your account.

- HTTP Method: `GET`
- Endpoint: `/legal-entities`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| type\_ | str | ❌ | Retrieve a list of legal entities in your account. |

**Return Type**

`LegalEntityListContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.organizations.get_legal_entity_list(type_="type")

print(result)
```

#### **get_organizations**

Retrieve the current organization details. Organization is automatically detected from the auth token.

- HTTP Method: `GET`
- Endpoint: `/organizations`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|

**Return Type**

`OrganizationListContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.organizations.get_organizations()

print(result)
```

#### **get_teams**

Retrieve a list of teams in your organization.

- HTTP Method: `GET`
- Endpoint: `/teams`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|

**Return Type**

`TeamListContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.organizations.get_teams()

print(result)
```

#### **get_agreements**

This end-point returns a list of your agreements with Deel.

- HTTP Method: `GET`
- Endpoint: `/agreements`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| contract_id | str | ❌ | This end-point returns a list of your agreements with Deel. |
| limit | str | ❌ | This end-point returns a list of your agreements with Deel. |
| offset | str | ❌ | This end-point returns a list of your agreements with Deel. |

**Return Type**

`AgreementListContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.organizations.get_agreements(
    contract_id="contract_id",
    limit="50",
    offset="0"
)

print(result)
```

#### **get_departments**

Get list of organization departments.

- HTTP Method: `GET`
- Endpoint: `/departments`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|

**Return Type**

`DepartmentsContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.organizations.get_departments()

print(result)
```

#### **get_working_locations**

Get organization working locations.

- HTTP Method: `GET`
- Endpoint: `/working-locations`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|

**Return Type**

`WorkingLocationsContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.organizations.get_working_locations()

print(result)
```

### LookupsService

A list of all methods in the `LookupsService` service. Click on the method name to view detailed information about that method.

| Methods                                         | Description                                                                 |
| :---------------------------------------------- | :-------------------------------------------------------------------------- |
| [get_countries](#get_countries)                 | Retrieve a list of countries supported by Deel.                             |
| [get_currencies](#get_currencies)               | Retrieve the list of currencies used by Deel.                               |
| [get_job_title_list](#get_job_title_list)       | Retrieve a list of pre-defined job titles in Deel platform.                 |
| [get_seniority_list](#get_seniority_list)       | Retrieve a list of pre-defined seniority level for roles in Deel platform.  |
| [get_timeoff_type_list](#get_timeoff_type_list) | Retrieve a list of pre-defined time off types to register in Deel platform. |

#### **get_countries**

Retrieve a list of countries supported by Deel.

- HTTP Method: `GET`
- Endpoint: `/lookups/countries`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|

**Return Type**

`CountryListContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.lookups.get_countries()

print(result)
```

#### **get_currencies**

Retrieve the list of currencies used by Deel.

- HTTP Method: `GET`
- Endpoint: `/lookups/currencies`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|

**Return Type**

`CurrencyListContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.lookups.get_currencies()

print(result)
```

#### **get_job_title_list**

Retrieve a list of pre-defined job titles in Deel platform.

- HTTP Method: `GET`
- Endpoint: `/lookups/job-titles`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| limit | float | ❌ | Retrieve a list of pre-defined job titles in Deel platform. |
| after_cursor | str | ❌ | Retrieve a list of pre-defined job titles in Deel platform. |

**Return Type**

`JobTitleListContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.lookups.get_job_title_list(
    limit=99,
    after_cursor="after_cursor"
)

print(result)
```

#### **get_seniority_list**

Retrieve a list of pre-defined seniority level for roles in Deel platform.

- HTTP Method: `GET`
- Endpoint: `/lookups/seniorities`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| limit | float | ❌ | Retrieve a list of pre-defined seniority level for roles in Deel platform. |

**Return Type**

`SeniorityListContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.lookups.get_seniority_list(limit=50)

print(result)
```

#### **get_timeoff_type_list**

Retrieve a list of pre-defined time off types to register in Deel platform.

- HTTP Method: `GET`
- Endpoint: `/lookups/time-off-types`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|

**Return Type**

`TimeoffTypeListContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.lookups.get_timeoff_type_list()

print(result)
```

### WebhooksService

A list of all methods in the `WebhooksService` service. Click on the method name to view detailed information about that method.

| Methods                                                             | Description                               |
| :------------------------------------------------------------------ | :---------------------------------------- |
| [get_all_webhooks](#get_all_webhooks)                               | Retrieve a list of webhook subscriptions. |
| [create_webhook](#create_webhook)                                   | Create a new webhooks subscription.       |
| [webhook_controller_get_by_id](#webhook_controller_get_by_id)       | Retrieve a single webhook subscription.   |
| [webhook_controller_edit_by_id](#webhook_controller_edit_by_id)     | Edit a webhook subscription.              |
| [webhook_controller_delete_by_id](#webhook_controller_delete_by_id) | Delete a webhook subscription.            |
| [get_all_webhook_event_types](#get_all_webhook_event_types)         | Retrieve a list of webhook event types.   |

#### **get_all_webhooks**

Retrieve a list of webhook subscriptions.

- HTTP Method: `GET`
- Endpoint: `/webhooks`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|

**Return Type**

`WebhookListResponse`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.webhooks.get_all_webhooks()

print(result)
```

#### **create_webhook**

Create a new webhooks subscription.

- HTTP Method: `POST`
- Endpoint: `/webhooks`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | CreateWebhookRequest | ✅ | The request body. |

**Return Type**

`WebhookItemResponse`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import CreateWebhookRequest

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CreateWebhookRequest(**{
    "name": "My first webhook.",
    "description": "I like it very much.",
    "status": "enabled",
    "url": "https://mywebhook.com",
    "signing_key": "signing_key",
    "api_version": "v2",
    "events": [
        "events"
    ]
})

result = sdk.webhooks.create_webhook(request_body=request_body)

print(result)
```

#### **webhook_controller_get_by_id**

Retrieve a single webhook subscription.

- HTTP Method: `GET`
- Endpoint: `/webhooks/{id}`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| id\_ | str | ✅ | Retrieve a single webhook subscription. |

**Return Type**

`WebhookItemResponse`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.webhooks.webhook_controller_get_by_id(id_="id")

print(result)
```

#### **webhook_controller_edit_by_id**

Edit a webhook subscription.

- HTTP Method: `PATCH`
- Endpoint: `/webhooks/{id}`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request*body | PatchWebhookRequest | ✅ | The request body. |
| id* | str | ✅ | Edit a webhook subscription. |

**Return Type**

`WebhookItemResponse`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import PatchWebhookRequest

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = PatchWebhookRequest(**{
    "name": "Demo webhook",
    "description": "My first webhook",
    "status": "enabled",
    "url": "https://mywebhook.com/listening",
    "signing_key": "signing_key",
    "api_version": "v2",
    "events": [
        "events"
    ]
})

result = sdk.webhooks.webhook_controller_edit_by_id(
    request_body=request_body,
    id_="id"
)

print(result)
```

#### **webhook_controller_delete_by_id**

Delete a webhook subscription.

- HTTP Method: `DELETE`
- Endpoint: `/webhooks/{id}`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| id\_ | str | ✅ | Delete a webhook subscription. |

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.webhooks.webhook_controller_delete_by_id(id_="id")

print(result)
```

#### **get_all_webhook_event_types**

Retrieve a list of webhook event types.

- HTTP Method: `GET`
- Endpoint: `/webhooks/events/types`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|

**Return Type**

`WebhookEventTypeListResponse`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.webhooks.get_all_webhook_event_types()

print(result)
```

### TokenService

A list of all methods in the `TokenService` service. Click on the method name to view detailed information about that method.

| Methods                                     | Description                                                     |
| :------------------------------------------ | :-------------------------------------------------------------- |
| [create_public_token](#create_public_token) | Create a public token to use with embedded Deel SDK components. |

#### **create_public_token**

Create a public token to use with embedded Deel SDK components.

- HTTP Method: `POST`
- Endpoint: `/public-tokens`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| request_body | CreatePublicTokenContainer | ✅ | The request body. |

**Return Type**

`PublicTokenCreatedContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment
from deel_sdk.models import CreatePublicTokenContainer

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CreatePublicTokenContainer(**{
    "data": {
        "scope": [
            "contracts:read"
        ]
    }
})

result = sdk.token.create_public_token(request_body=request_body)

print(result)
```

### CartaService

A list of all methods in the `CartaService` service. Click on the method name to view detailed information about that method.

| Methods                                             | Description                          |
| :-------------------------------------------------- | :----------------------------------- |
| [get_equity_stakeholders](#get_equity_stakeholders) | Retrieve all stakeholders for Carta. |

#### **get_equity_stakeholders**

Retrieve all stakeholders for Carta.

- HTTP Method: `GET`
- Endpoint: `/equity/stakeholders`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| limit | float | ❌ | Retrieve all stakeholders for Carta. |
| cursor | str | ❌ | Retrieve all stakeholders for Carta. |

**Return Type**

`EquityStakeholdersContainer`

**Example Usage Code Snippet**

```py
from deel_sdk import DeelSdk, Environment

sdk = DeelSdk(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.carta.get_equity_stakeholders(
    limit=10,
    cursor="cursor"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
