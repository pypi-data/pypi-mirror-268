from typing import Dict

from circles_local_aws_s3_storage_python import StorageConstants
from circles_local_aws_s3_storage_python.CirclesStorage import circles_storage
from database_mysql_local.point import Point
from email_address_local.email_address import EmailAddressesLocal
from gender_local.gender import Gender
from group_profile_remote.group_profile import GroupProfilesRemote
from group_remote.group_remote import GroupsRemote
from language_remote.lang_code import LangCode
from location_local.locations_local_crud import LocationsLocal
from logger_local.MetaLogger import MetaLogger
from operational_hours_local.src.operational_hours import OperationalHours
from profile_profile_local.src.profile_profile import ProfileProfile
from profile_reaction_local.src.profile_reaction import ProfileReactions
from reaction_local.reaction import ReactionsLocal

from .constants_profiles_local import PROFILE_LOCAL_PYTHON_LOGGER_CODE, DEFAULT_LANG_CODE
from .profiles_local import ProfilesLocal


class ComprehensiveProfilesLocal(metaclass=MetaLogger, object=PROFILE_LOCAL_PYTHON_LOGGER_CODE):
    def __init__(self):
        self.location_local = LocationsLocal()
        self.profiles_local = ProfilesLocal()
        self.storage = circles_storage()
        self.gender = Gender()
        self.profile_profile = ProfileProfile()
        self.group_profiles_remote = GroupProfilesRemote()
        self.email_addresses_local = EmailAddressesLocal()
        self.operational_hours = OperationalHours()
        self.reaction = ReactionsLocal()

    def insert(self, profile_json: dict, lang_code: LangCode) -> int:
        """Returns the profile_id of the inserted profile"""

        profile_id = location_id = None

        if "location" in profile_json:
            location_entry: Dict[str, any] = profile_json["location"]
            location_data: Dict[str, any] = {
                "coordinate": Point(longitude=location_entry["coordinate"].get("latitude"),
                                    latitude=location_entry["coordinate"].get("longitude")),
                "address_local_language": location_entry.get("address_local_language"),
                "address_english": location_entry.get("address_english"),
                "postal_code": location_entry.get("postal_code"),
                "plus_code": location_entry.get("plus_code"),
                "neighborhood": location_entry.get("neighborhood"),
                "county": location_entry.get("county"),
                "region": location_entry.get("region"),
                "state": location_entry.get("state"),
                "country": location_entry.get("country")
            }
            location_id = self.location_local.insert(data=location_data, lang_code=lang_code, is_approved=False)

        # Insert person to db
        if 'person' in profile_json:
            # TODO person_entry -> person_dict
            person_entry: Dict[str, any] = profile_json['person']

            # TODO I would expect the 1st thing we do with person_dict is "person: PersonLocal(person_dict)". Can we do this approach on all entities?

            # TODO: I prefer we use "person.getGender()"
            gender_id = self.gender.get_gender_id_by_title(person_entry.get('gender'))
            person_data: Dict[str, any] = {
                'last_coordinate': person_entry.get('last_coordinate'),
            }
            # TODO: Why do we need gender_id and person_data?
            # Person class has errors - TODO Let's fix them
            '''
            person_dto = PersonDto(
                gender_id, person_data.get('last_coordinate'),
                person_data.get('location_id'))

            # TODO We prefer PersonsLocal.insert(person) which updates both person_table and person_ml_table
            person_id = PersonsLocal.insert(person_dto)
            PersonsLocal.insert_person_ml(
                person_id,
                lang_code,
                person_data.get('first_name'),
                person_data.get('last_name'))
            '''

        # Insert profile to db
        if 'profile' in profile_json and 'person_id' in profile_json.get("person", {}):
            profile_id = self.profiles_local.insert(profile_json=profile_json['profile'],
                                                    person_id=profile_json['person']['person_id'])

        # insert profile_profile to db
        if 'profile_profile' in profile_json:
            profile_profile_entry: Dict[str, any] = profile_json['profile_profile']
            for i in profile_profile_entry:
                profile_profile_part_entry: Dict[str, any] = profile_profile_entry[i]
                profile_profile_data: Dict[str, any] = {
                    'profile_id': profile_profile_part_entry.get('profile_id'),
                    'relationship_type_id': profile_profile_part_entry.get('relationship_type_id'),
                    'job_title': profile_profile_part_entry.get('job_title', None)
                }
                profile_profile_id = self.profile_profile.insert_profile_profile(
                    profile_id1=profile_profile_data['profile_id'], profile_id2=profile_id,
                    relationship_type_id=profile_profile_data['relationship_type_id'],
                    job_title=profile_profile_data['job_title'])
                self.logger.info(object={"profile_profile_id": profile_profile_id})

        # insert group to db
        if 'group' in profile_json:
            group_entry: Dict[str, any] = profile_json['group']
            group_id = GroupsRemote().create_group(title=group_entry.get('title'),
                                                   title_lang_code=group_entry.get('lang_code', DEFAULT_LANG_CODE).value,
                                                   parent_group_id=group_entry.get('parent_group_id'),
                                                   is_interest=group_entry.get('is_interest'),
                                                   image=group_entry.get('image', None))
            self.logger.info(object={"group_id": group_id})

        # insert group_profile to db
        if 'group_profile' in profile_json:
            group_profile_entry: Dict[str, any] = profile_json['group_profile']
            group_profile_data: Dict[str, any] = {
                'group_id': group_profile_entry.get('group_id'),
                'relationship_type_id': group_profile_entry.get('relationship_type_id'),
            }
            group_profile_id = self.group_profiles_remote.create(
                group_id=group_profile_data['group_id'],
                relationship_type_id=group_profile_data['relationship_type_id'])
            self.logger.info(object={"group_profile_id": group_profile_id})

        # insert email to db
        if 'email' in profile_json:
            email_entry: Dict[str, any] = profile_json['email']
            email_address_json: Dict[str, any] = {
                'email_address': email_entry.get('email_address'),
                'lang_code': email_entry.get('lang_code', DEFAULT_LANG_CODE).value,
                'name': email_entry.get('name'),
            }
            email_address_id = self.email_addresses_local.insert(
                email_address_json['email_address'], LangCode[email_address_json['lang_code']],
                email_address_json['name'])
            self.logger.info(object={"email_address_id ": email_address_id})

        # Insert storage to db
        if "storage" in profile_json:
            storage_data = {
                "path": profile_json["storage"].get("path"),
                "filename": profile_json["storage"].get("filename"),
                "region": profile_json["storage"].get("region"),
                "url": profile_json["storage"].get("url"),
                "file_extension": profile_json["storage"].get("file_extension"),
                "file_type": profile_json["storage"].get("file_type")
            }
            if storage_data["file_type"] == "Profile Image":
                self.storage.save_image_in_storage_by_url(image_url=storage_data["url"],
                                                          local_filename=storage_data["filename"],
                                                          profile_id=profile_id,
                                                          entity_type_id=StorageConstants.PROFILE_IMAGE),

        # Insert reaction to db
        if "reaction" in profile_json:
            reaction_json = {
                "value": profile_json["reaction"].get("value"),
                "image": profile_json["reaction"].get("image"),
                "title": profile_json["reaction"].get("title"),
                "description": profile_json["reaction"].get("description"),
            }

            reaction_id = self.reaction.insert(reaction_json, lang_code)
            # Insert profile-reactions to db
            ProfileReactions.insert(reaction_id, profile_id)

        # Insert operational hours to db
        if "operational_hours" in profile_json:
            operational_hours_list_of_dicts = OperationalHours.create_hours_array(
                profile_json["operational_hours"])
            self.operational_hours.insert(profile_id, location_id, operational_hours_list_of_dicts)

        return profile_id
