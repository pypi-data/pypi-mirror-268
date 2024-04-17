# Black Duck License Utilities

This module delivers functionality for 
* License Conflicts
* License Tagging and Grouping

## Requirements
Module requires Python 3.8 or higher.
The following modules are required:
* argparse
* blackduck
* openpyxl

## Installation

Module is installed using pip command
```
pip3 install blackduck-lutils
```

## License Conflicts

### Description
This functionality will generate license conflict report by comparing license terms of the licenses associated with components on the Bill of Materials.
Project version license will be taken into account and license conflicts for it will be calculated as well.

### How it works
The process is designed to minimize API calls required to produce a report. This is achieved by putting license information into a local storage file and utilizing SBOM report as the data source for project information.

License conflicts defines two main functions
* download_license_data - used to download license data during bootstrapping process
* generate_license_conflict_report - core functionality

MOdule provides main() function to allow either direct execution or integrating into larger automation.

### Bootstrapping
Before using the script, license data would have to be downloaded from the system and stored in to a file. To perform that task using direct execution perform the following:

```
python3 -m blackduck_lutils.license_conflicts -u $BD_URL -t token_file -nv -ldd [-ld license_data.json]
```

This will download license data into 'license_data.json` file in the current directory. To place the file into different location use corresponding command line option.

Same task can be accomplished with the following code:

```
from blackduck_lutils import license_conflicts

license_conflicts.download_license_data(base_url=blackduck_url, 
                                        token=token, 
                                        no_verify=no_verify_flag, 
                                        output_file = license_data_filename)
```

Note: This operation will execute about 3000 API calls and that is primarily the reason why we put this data into local storage. This way we don't have to put that much load onto the server when generating conflict reports.

Note: This file would have to be regenerated if new licenses are added to the system.

### Generating Conflict Report
This utility cam be used in off-line and on-lne modes.

#### On-line mode
In on-line mode the following actions will take place:
* Issue an API request to generate SBOM report.
* Wait for report completion
* Download the report 
* Generate license conflicts data and write it into CSV file

To generate License Conflict Report in on-line mode using direct execution perform the following:

```
python3 -m blackduck_lutils.license_conflicts -u $BD_URL -t token -nv -pn ProjectName -pv ProjectVersion \
                                              [-ld license_data.json] [-o output_file]
```
Where $BD_URL is the URL of your Black Duck system and 'token' is a file containing API token.

Same task can be accomplished with the following code:
```
from blackduck_lutils import license_conflicts

license_conflicts.generate_license_conflict_report(base_url=blackduck_url, 
                                                  token=token_file, 
                                                  no_verify=no_verify_flag, 
                                                  project_name=project_name, 
                                                  project_version_name=project_version_name,
                                                  license_data_file=license_data_file,
                                                  csv_report_file=output_file)

```

#### Off-line mode
In off-line mode a SBOM report in SPDX format would have to exist.
The following actions will take place:
* Load SBOM report from a file
* Generate license conflict data and write it into a file

To generate License Conflict Report in off-line mode using direct execution perform the following:

```
python3 -m blackduck_lutils.license_conflicts -u $BD_URL -t token -nv -sbom SBOM_FILE \
                                              [-ld license_data.json] [-o output_file]
```
Where $BD_URL is the URL of your Black Duck system and 'token' is a file containing API token.

Same task can be accomplished with the following code:

```
from blackduck_lutils import license_conflicts

license_conflicts.generate_license_conflict_report(sbom=SBOM_FILE, 
                                 license_data_file=license_data_file,
                                 csv_report_file=output_file)

```

### Module Command Line specification

```
$ python3 -m blackduck_lutils.license_conflicts -h
usage: license_conflicts [-h] -u BASE_URL -t TOKEN_FILE [-nv] [-ldd] [-pn PROJECT_NAME]
                                 [-pv PROJECT_VERSION_NAME] [-sbom SBOM] [-ld LICENSE_DATA] [-o OUTPUT_FILE]

options:
  -h, --help            show this help message and exit
  -u BASE_URL, --base-url BASE_URL
                        Hub server URL e.g. https://your.blackduck.url
  -t TOKEN_FILE, --token-file TOKEN_FILE
                        File containing access token
  -nv, --no-verify      Disable TLS certificate verification
  -ldd, --license-data-download
                        Download license data into a file specified with -ld/--license-data parameter
  -pn PROJECT_NAME, --project-name PROJECT_NAME
                        Project Name
  -pv PROJECT_VERSION_NAME, --project-version-name PROJECT_VERSION_NAME
                        Project Version Name
  -sbom SBOM            SBOM File to process
  -ld LICENSE_DATA, --license-data LICENSE_DATA
                        Local license data storage
  -o OUTPUT_FILE, --output-file OUTPUT_FILE
                        CSV file name for license conflict report output
$
```

### Results
Conflict report will be written into CSV file with one line per license term conflict.
The following fields will be present in the file:
* Category
* ComponentName
* ComponentLicense
* ConflictingComponentName
* ConflictingComponentLicense
* ConflictingLicenseTerm
* TermValue
* ConflictingTermValue
* TermDescription
* ConflictingTermDescription

### TODO
This utility is tested in off-line and online mode and has sufficient functionality for API performance testing.

It is not fully tested against functional specification yet.


### License
This utility is licenses under Apache 2.0 License.


## License Tagging and Grouping
License tagging and grouping to allow easy insertion of arbitrary groups of licenses into policy definitions. 

### Description
When there is a need to add an arbitrary group of licenses into a Black Duck policy
it requires adding them one by one through the UI. This tool allows to maintain an external data store with Tags ang Tag mappings to the licenses and will allow updating policy definitions with expanded list of licenses.

### Usage
Tool can be executed as a direct module execution with the following command line specification:

```
$ python3 -m blackduck_lutils.license_tagging -h
usage: license_tagging [-h] -u BASE_URL -t TOKEN_FILE [-nv] [-lsf LICENSE_STORE_FILE] [-nlc]

options:
  -h, --help            show this help message and exit
  -u BASE_URL, --base-url BASE_URL
                        Hub server URL e.g. https://your.blackduck.url
  -t TOKEN_FILE, --token-file TOKEN_FILE
                        File containing access token
  -nv, --no-verify      Disable TLS certificate verification
  -lsf LICENSE_STORE_FILE, --license-store-file LICENSE_STORE_FILE
                        Local license information storage
  -nlc, --no-license-check
                        Skip scanning trough all licenses

### How it works
The tool maintains local local data storage as an Excel file with default filename of 'LicenseStorage.xlsx'

This file will contain two worksheets
- Licenses
- LicenseTags

Licenses worksheet contains data on all licenses currently present in Black Duck instance. Columns contain data and are used as following:
* Column A - License Name
* Column B - License URL
* Column C - License Family
* Column D - License Family URL
* Column E - SPDXID
* Column F and above can contain tags

LicenseTags worksheet contains License Tag Names in the Column A and corresponding URL in column B. 

#### Common parameters
In the example command line there would be references to common parameters:
* $BD_URL - environment variable containing Black Duck instance URL
* token. - a text file containing valid authentication token

#### Bootstrapping
Before using the tool, local storage would have to be initialized.
That is accomplished by running the script.  If it can not find local license store, it will generate new file with complete internal structures and populate Licenses worksheet with data from Black Duck instance.

```
python3 -m blackduck_lutils.license_tagging -u $BD_URL -t token -nv
```

This will generate a file named LicenseStorage.xlsx in the current folder and populate Licenses worksheet with full complement of licenses from your Black Duck instance.

It will also validate presence of 'TagPlaceholder' and create it as necessary.
At this point there will be no tags defined yet.

#### Defining tags
User must open the local store excel file and add tags to Column A of LicenseTag worksheet, save the Excel file and run the script again.
```
python3 -m blackduck_lutils.license_tagging -u $BD_URL -t token -nv
```
This action will update the references in Black Duck and get the framework ready to be used.

#### Tagging Licenses
Using Excel as a tool, tag licenses on the License worksheet by putting tag name in the columns F and above. There is no limit on how many tags could be associated with a license. 

#### Policy creation
When creating a policy that would have to reference large number of licenses use TagName which will be visible and searchable in the UI.

#### Expanding tags to full list of licenses
Execute the script again and the Tags in the policy will be expanded to full list of licenses.
```
python3 -m blackduck_lutils.license_tagging -u $BD_URL -t token -nv
```
This action will iterate through the policies, find policy conditions that have tag name in them and replace them with corresponding list of licenses.

### Example of use
See example of use here

### License
This code is licensed under Apache 2.0 license.

### Project status
Active
