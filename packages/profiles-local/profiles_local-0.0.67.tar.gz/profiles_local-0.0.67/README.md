# Installation and upgrade

To install this package run `pip install -U profiles-local`

# Import

`from profiles_local.comprehensive_profile import ComprehensiveProfilesLocal`

# Use example

```json
data = {
  'location': LOCATION_DATA,
  'profile': PROFILE_DATA,
  'storage': STORAGE_DATA,
  'reaction': REACTION_JSON,
  'operational_hours': OPERATIONAL_HOURS
}
```

Where LOCATION_DATA, PROFILE_DATA, STORAGE_DATA, REACTION_JSON, OPERATIONAL_HOURS are dictionaries with the relevant
data for the table.  
i.e. for profile_table:

```json
PROFILE_DATA = {
  'name': NAME,
  'name_approved': NAME_APPROVED,
  'lang_code': LANG_CODE,
  'user_id': USER_ID,
  'is_main': IS_MAIN,
  'visibility_id': VISIBILITY_ID,
  'is_approved': IS_APPROVED,
  'profile_type_id': PROFILE_TYPE_ID,
  'preferred_lang_code': PREFERRED_LANG_CODE,
  'experience_years_min': EXPERIENCE_YEARS_MIN,
  'main_phone_id': MAIN_PHONE_ID,
  'is_rip': is_rip,
  'gender_id': GENDER_ID,
  'stars': STARS,
  'last_dialog_workflow_state_id': LAST_DIALOG_WORKFLOW_STATE_ID
}
```

Now we can call the generic_profile_insert function:  
`profile_id = ComprehensiveProfilesLocal.insert(data)`

If the function inserted a profile successfully it returns the profile_id of the inserted profile.  
The function doesn't have to always insert a profile, for example you can use it to insert only a location with
`data = {'location': LOCATION_DATA}`

and then the returned profile_id will be 'None'.