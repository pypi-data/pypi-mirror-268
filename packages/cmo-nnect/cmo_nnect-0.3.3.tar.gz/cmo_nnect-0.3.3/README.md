# Cmotions Nnect (Cmo-Nnect)

cmo_nnect is a Python library created by [Cmotions](https://cmotions.nl/). This library aims to ease the interaction with different API's of software packages. Examples include Microsoft Dynamics, Exact Online, AFAS Profit etc. You only need the right authentication credentials, and the target endpoints of the source/destination API to start interacting!

From our experience with integrating data from a variety of software packages we decided to publish our connectors to ease the use of the API's with Python. We encourage collaboration to increase the number of connectors and improvements of existing connectors!

The package has parallelization functionality built in for most connectors. This means that you are able to provide a list of entities/tables/endpoints and they are retrieve from the data source in parallel.

The library always returns a Pandas dataframe by default, or if you provide a list, it will return a dictionary with "entityname":"dataframe" key-valuepairs.

## Table of contents

- [Installation](#installation)
- [Usage](#usage)
- [AFAS Profit](#afasprofit) (afasprofit)
- [Braze](#braze) (braze)
- [Business Central](#businesscentral) (businesscentral)
- [Dynamics 365](#dynamics365) (dynamics365)
- [Exact](#exact) (exact)
- [Freshdesk](#freshdesk) (freshdesk)
- [Freshsales](#freshsales) (freshsales)
- [Google Analytics](#ga4) (ga4)
- [Kadaster](#kadaster) (kadaster)
- [KNMI](#knmi) (knmi)
- [Mautic](#mautic) (mautic)
- [Notion](#notion) (notion)
- [Piano](#piano) (piano)
- [Recruitee](#recruitee) (recruitee)
- [Salesforce Marketing Cloud](#salesforcemarketingcloud) (sfmc)
- [Contributing](#contributing)
- [License](#license)
- [Contributors](#contributors)

<a id="installation"></a>

## Installation

Install cmo_nnect using pip

```bash
pip install cmo-nnect
```

<a id="usage"></a>

## Usage

Choose the [connector](#Available-connectors) from the list, and import the connector by using the reference name. For example for AFAS Profit the reference name is afasprofit:

```python
from cmo_nnect import afasprofit
```

From the [connector usage documentation](#Connector-usage) determine the authentication requirements, for example for AFAS Profit we need a token, a company-id, and an optional environment name. We can then initialize a client:

```python
# define authentication credentials
token = "<token><version>1</version><data>54740093832496081845474abcdefghijklmnopq740093832496081841234127</data></token>"
company_id = 12345
environment = "development"

# set up a client to ease interaction
client = afasprofit(token,company_id)
```

We are now able to start interacting with the API. To extract data you can use the format client.get_data(). In the documentation of the specific connector you can see what is expected for the specific method. For example for AFAS Profit we need to provide a get_connector name, and optional parameters:

```python
# define parameters
params = {"skip": "-1", "take": "-1"}

# extract data from the software package
contacts = client.get_data("get_contacts", params)
```

The package automatically parallelizes the processing when you provide a list of entities, where possible. If you are using this package in production, this would be the preferred way to ingest data.

<a id="afasprofit"></a>

## AFAS Profit

**Import**<br>

```python
from cmo_nnect import afasprofit
```

**Authentication**<br>
To authenticate with AFAS Profit you need:

- A profit token (e.g. "<token><version>1</version><data>54740093832496081845474abcdefghijklmnopq740093832496081841234127</data></token>")
- A company ID (e.g. 12345)
  Optionally:
- An environment, defaults to production (e.g. "test")

**Interaction**<br>
For each interaction you can provide optional parameters in a dictionary (e.g. {"skip": "-1", "take": "-1"}).

**Extracting data**<br>
To get data, you need:

- A get_connector name of a get connector or a list of get connectors which is [set-up in AFAS profit](https://help.afas.nl/help/NL/SE/App_Apps_Custom_Add.htm) (e.g. "get_contacts")

<a id="braze"></a>

## Braze

**Import**<br>

```python
from cmo_nnect import braze
```

**Authentication**<br>
To authenticate with Braze you need:

- A Braze api key (e.g. "sfgs3456-3456-7889-b134-sadfg32431f")

Optionally:

- An instance name of your region, defaults to europe 1 ("fra-01")

**Interaction**<br>
For each interaction you can provide parameters (e.g. campaign_id=adfa9-af89a-ad9f8f&length=2).

**Extracting data**<br>
To get data, you need:

- An endpoint name or a list of endpoint names which you can find in the [Braze API Documentation](https://www.braze.com/docs/api/basics/#endpoints) (e.g. "campaigns/list")

<a id="businesscentral"></a>

## Business Central

**Import**<br>

```python
from cmo_nnect import businesscentral
```

**Authentication**<br>
To authenticate with Business Central you need an app registration in Azure Active Directory which has the correct access rights in Business Central.

Then you need:

- A Client ID (e.g. "f1234562-978c-4ae6-886e-eb0e90043775"), belonging to the app registration
- A Client Secret (e.g. "a1238Q~5.sadf324235.5lhevWdAql_ai.bmSA"), belonging to the app registration
- A Tenant ID (e.g. "fcea12312c-cd2a-45b6-8a44-11a1b7165ccc"), id of the Azure Tenant where the app registration was made
- An Environment ID (e.g. "DEV"), name of environment you want to interact with

**Interaction**<br>
After initializing, you get an overview of the available companies. The default interaction is to retrieve data for all companies, but you are able to specify only one company-ID when making requests to only retrieve data for one company.

**Extracting data**<br>
To get data, you need:

- An endpoint name or a list of endpoint names which you can find in the [Business Central API Documentation](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/) (e.g. "customers")

OR

- A custom entity name or a list of custom entity names, for which you need to specify the parameter <i>odata=True</i>

<a id="dynamics365"></a>

## Dynamics 365

**Import**<br>

```python
from cmo_nnect import dynamics365
```

**Authentication**<br>
To authenticate with Dynamics 365 you need:

- A Client id(e.g. "831fc512-1352-4c0d-af44-99af61e4dfd7")
- A Client Secret of your app registration (e.g. ~WiJDFjfodj09uf8a9f)
- A tenant id, Tenant Application Identity (e.g. "sfgs3456-3456-7889-b134-sadfg32431f")
- An URL (e.g. "https://api.businesscentral.dynamics.com/v2.0/")

**Interaction**<br>
For each interaction you can provide optional parameters in a dictionary (e.g. "$filter=modifiedon gt 2018-01-01"). You can also provide the parameter Fo = True if you want to extract data from specifically Finance & Operations.

**Extracting data**<br>
To get data, you need:

- An entity name or a list of entity names which is you can find in the [Dynamics documentation](https://statics.teams.cdn.office.net/evergreen-assets/safelinks/1/atp-safelinks.html) (e.g. "Account")

<a id="Exact"></a>

## Exact

**Import**<br>

```python
from cmo_nnect import exact
```

**Authentication**<br>
To authenticate with Exact you need:

- Exact base url (e.g. "https://start.exactonline.nl")
- A Exact client id (e.g. "sfgs3456-3456-7889-b134-sadfg32431f")
- A Exact client secret (e.g. "~Waifjdfaklf0889dhf")
- SecretManagement Class (e.g. "SecretManagement.Env(env_variabele='exact_config')")

Optionally:

- authenticate, defaults to False. This boolean is used start the authenication flow of Exact, where we need to login into the browser and copy the code received into the input in order to receive our Exact config file with access_token and refresh_token. Only use the authentication flow if you use the connector for the first time or if you want to regenerate the Exact config file.

**Interaction**<br>
To initialize the Exact connector you need to provide a SecretManagement class. You can import the class using:
`from cmo_nnect.helpers import SecretManagement`.
The SecretManagement class has mutiple subclasses to store your secrets (e.g. KeyVault, Env or File). The way the secrets are stored are based on the subclass you choose. For example if we want to store the secrets in an environment variable we can initialize our SecretManagement class as follows: `SecretManagement.Env(env_variable="your_env_variable")`. This will make sure the secrets used in the Exact connector are stored in and extracted from your chosen environment variable.

**Extracting data**<br>
To get data, you need:

- An endpoint name or a list of endpoint names which you can find in the [Exact API Documentation](https://start.exactonline.nl/docs/HlpRestAPIResources.aspx) (e.g. "Budgets")

<a id="freshdesk"></a>

## Freshdesk

**Import**<br>

```python
from cmo_nnect import freshdesk
```

**Authentication**<br>
To authenticate with Freshdesk you need:

- Your domain name, which you can find in the url of your freshdesk environment (e.g. "cmotions").
- A Personal API key, which you can find in the Support Portal (e.g. "akdfjaoidfj809afauihf")

**Extracting data**<br>
To get data, you need:

- An endpoint name or a list of endpoints which you can find in the [Freshdesk API documentation](https://developers.freshdesk.com/api/?_gl=1*zrdhn3*_ga*MTc5MzIwNzQyNS4xNjk0Njk2NzEz*_ga_5S1FBQDGB1*MTY5NDY5NjcxMy4xLjAuMTY5NDY5NjcxNi41Ny4wLjA.&_ga=2.122097288.2046862385.1694696713-1793207425.1694696713#introduction) (e.g. "tickets")

Optionally:

- Set pagination to True or False, defaults to False. If you set pagination to True the connector will retrieve all the records available by using the pagination links of the Freshdesk API.

<a id="freshsales"></a>

## Freshsales

**Import**<br>

```python
from cmo_nnect import freshsales
```

**Authentication**<br>
To authenticate with Freshsales you need:

- Your domain name, which you can find in the url of your freshsales environment (e.g. "cmotions").
- A Personal API key, which you can find in the Portal under Profile Settings (e.g. "akdfjaoidfj809afauihf")

**Extracting data**<br>
To get data, you need:

- An endpoint name or a list of endpoints which you can find in the [Freshsales API documentation](https://developers.freshworks.com/crm/api/#introduction) (e.g. "/api/contacts/30000912")

Optionally:

- Set pagination to True or False, defaults to False. If you set pagination to True the connector will retrieve all the records available by using the pagination links of the Freshsales API.

<a id="ga4"></a>

## Google Analytics

**Import**<br>

```python
from cmo_nnect import ga4
```

**Authentication**<br>
To authenticate with Google Analytics you need:

- key_file_location, path to the keyfile generated by Google Cloud (e.g. "./path/to/keyfile.json")
- or the contents of the key file as JSON string (e.g. stored as secret in a key vault)
- property_id, The id of the Google Analytics property you wish to connect to (e.g. "12391249761")

**Extracting data**<br>
To get data, you need:

- A starting_date and ending_date formatted in YYYY-MM-dd, NdaysAgo, yesterday, or today (e.g. 2023-09-01 or 30daysAgo)
- A list of metrics and dimensions found in the [Google Analytics Documentation](https://support.google.com/analytics/answer/9143382?hl=en) (e.g. ["ga:date", "ga:sourceMedium"]). You can also choose to request a print of available metrics and dimensions by initializing the Ga4 class with get_metadata = True

<a id="kadaster"></a>

## Kadaster

**Import**<br>

```python
from cmo_nnect import kadaster
```

**Authentication**<br>
To authenticate with AFAS Profit you need:

- An API key, which you can request on the [Kadaster website](https://www.kadaster.nl/zakelijk/producten/adressen-en-gebouwen/bag-api-individuele-bevragingen) (e.g. "l7f0d14f0675774de181b1137fe99bdeb6")

**Interaction**<br>
For each interaction you can provide optional parameters in the relative URL.

**Extracting data**<br>
To get data, you need:

- A relative endpoint or a list of relative endpoints, which you can find in the [Kadaster GitHub](https://github.com/lvbag/BAG-API/blob/master/Documentatie/Tabel_Wat%20zit%20in%20welk%20endpoint_.pdf) (e.g. "/adressen")

<a id="knmi"></a>

## KNMI

**Import**<br>

```python
from cmo_nnect import knmi
```

**Authentication**<br>
No authentication is needed to use the KNMI connector.

**Interaction**<br>
For each interaction you can provide parameters (e.g. granularity=daggegevens&vars=TG:TN:TX:T10N).

**Extracting data**<br>
To get data, you need:

- A start and enddate which should be formatted as YYYYMMDD (e.g. "start=20231201&end=20231207")

Optionally:

- vars, different variables for different types of weather information (e.g. "vars=TG:TN:TX:T10N")
- stations, you can select from which weather stations you would like to recieve the data (defaults to all stations) (e.g. "stations=235:280:260")
- granularity, you can choose between "daggegevens" (daily) or "uurgegevens" (hourly) data (defaults to daily) (e.g. "granularity=daggegevens")

More information about the parameters can be found in the [KNMI API Documentation](https://www.knmi.nl/kennis-en-datacentrum/achtergrond/data-ophalen-vanuit-een-script).

<a id="mautic"></a>

## Mautic

**Import**<br>

```python
from cmo_nnect import mautic
```

**Authentication**<br>
To authenticate with Mautic you need:

- A company name, you can find the company name in the url of your mautic instance (e.g. cmotions)
- A client id, the client id will be generated when the mautic administrator enables the API. Check the [Mautic documentation](https://developer.mautic.org/#authorization) for setting this up.
- A client secret, the client secret will be generated when the mautic administrator enables the API. Check the [Mautic documentation](https://developer.mautic.org/#authorization) for setting this up.

**Interaction**<br>
For each interaction you can provide optional parameters in a dictionary (e.g. "limit=10&minimal=true").

**Extracting data**<br>
To get data, you need:

- A entity name of a list of entity names, check the [Mautic documentation](https://developer.mautic.org/#endpoints) for the available entities (e.g. "campaigns")

<a id="notion"></a>

## Notion

**Import**<br>

```python
from cmo_nnect import notion
```

**Authentication**<br>
To authenticate with Mautic you need:

- An API version (yyyy-MM-dd), you can find the latest Notion API version in the [documentation](https://developers.notion.com/reference/versioning).
- An access token, you can generate the API token in the Notion portal. Check the [Notion documentation](https://developers.notion.com/docs/authorization) for setting this up.

**Extracting data**<br>
To get data, you need:

- An endpoint or a list of endpoints, check the [Notion documentation](https://developers.notion.com/reference/intro) for the available entities (e.g. "users").
- A query, when your endpoint ends with "/query" you must provide a query in json format.
- Pagination, optionally you can set the pagination argument to True if you want to make use of pagination.

<a id="piano"></a>

## Piano Analytics

**Import**<br>

```python
from cmo_nnect import piano
```

**Authentication**<br>
To authenticate with Piano you need:

- An access key, which you can setup in your [profile page](https://user-profile.atinternet-solutions.com/#/apikeys) (e.g. "asdfadfad")
- An secret key, which you can setup in your [profile page](https://user-profile.atinternet-solutions.com/#/apikeys) (e.g. Ki98ahdf9uahdfH&FUDHF123fdq)
- Spaces, a list of site ids you want to query on (e.g. "[234234, 567567]")

**Interaction**<br>
For each interaction you can provide optional parameters; granularity, page_number, max_results, options, segment, filter (e.g. "granularity="H"). You can find the details in the [Piano API documentation](https://developers.atinternet-solutions.com/data-api-en/reporting-api-v3/getting-started/make-your-first-api-call-2/)

**Extracting data**<br>
To get data, you need:

- A list of column names (e.g. "[m_visits]")
- A list of start date in YYYY-MM-dd format (e.g. "2023-09-01")
- A list of end date in YYYY-MM-dd format (e.g. "2023-09-20")
- A list of sort (e.g. "[-m_visits]")

You can find the details in the [Piano API documentation](https://developers.atinternet-solutions.com/data-api-en/reporting-api-v3/getting-started/make-your-first-api-call-2/)

<a id="recruitee"></a>

## Recruitee

**Import**<br>

```python
from cmo_nnect import recruitee
```

**Authentication**<br>
To authenticate with Recruitee you need:

- An API Token, which you can generate in Recruitee application. Check the [Recruitee Documentation](https://docs.recruitee.com/reference/getting-started) for instructions (e.g. "HIkljai23fj3adfa4kj14dfnUUF")
- A company ID (e.g. 70003)

**Extracting data**<br>
To get data, you need:

- An endpoint name or a list of enpoint names which you can find in the [Recruitee Documentation](https://api.recruitee.com/docs/index.html#mailbox.web.mailbox-mailbox.web.mailbox-get-6) (e.g. "offers")

<a id="salesforcemarketingcloud"></a>

## Salesforce Marketing Cloud

**Import**<br>

```python
from cmo_nnect import sfmc
```

**Authentication**<br>
To authenticate with Salesforce Marketing Cloud you need:

- A Client ID (e.g. "adfadgadg089a7dfa")
- A Client Secret (e.g. "~adlfj0aufd0a89a7f0da89fh0a879fda98`")
- A Subdomain (e.g. "d98ads7a98df7").

Check the [Salesforce Marketing Cloud Documentation](https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/integration-s2s-client-credentials.html) for getting your client credentials.

**Extracting data**<br>
To get data, you need:

- A external key of the data entity you want to extract, the name of an [API endpoint](https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/routes.html) or a list of external keys or endpoints.
- Optionally you can provide the following parameters to adjust your output: filter, pageSize, orderby, top, skip & select.

<a id="contributing"></a>

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Please make sure to update tests as appropriate. You can find the repository [here](https://dev.azure.com/Cmotions/Packages/_git/cmo_nnect).

<a id="license"></a>

## License

[GNU General Public License v3.0](https://choosealicense.com/licenses/gpl-3.0/)

<a id="contributors"></a>

## Contributors

- Thijs van der Velden
- Koen Leijsten
- Jeroen Groothedde
- Adriaan Verhoeff
- Said Ouaali

[Contact us](mailto:info@cmotions.nl)
