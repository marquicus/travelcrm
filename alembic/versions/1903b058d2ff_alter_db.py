"""alter db

Revision ID: 1903b058d2ff
Revises: None
Create Date: 2014-04-30 16:36:21.314873

"""

# revision identifiers, used by Alembic.
revision = '1903b058d2ff'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('fk_resource_id_accomodation', 'accomodation', 'resource', ['resource_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_resource_id_address', 'address', 'resource', ['resource_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_location_id_address', 'address', 'location', ['location_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_resource_id_advsource', 'advsource', 'resource', ['resource_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_resource_id_appointment', 'appointment', 'resource', ['resource_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_employee_id_appointment', 'appointment', 'employee', ['employee_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_position_id_appointment', 'appointment', 'position', ['position_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_currency_id_appointment', 'appointment', 'currency', ['currency_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_resource_id_bank_detail', 'bank_detail', 'resource', ['resource_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_currency_id_bank_detail', 'bank_detail', 'currency', ['currency_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_bank_id_bank_detail', 'bank_detail', 'bank', ['bank_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_bank_id_bank_address', 'bank_address', 'bank', ['bank_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_address_id_bank_address', 'bank_address', 'address', ['address_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_resource_id_bank', 'bank', 'resource', ['resource_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_bperson_id_bperson_contact', 'bperson_contact', 'bperson', ['bperson_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_contact_id_bperson_contact', 'bperson_contact', 'contact', ['contact_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_resource_id_bperson', 'bperson', 'resource', ['resource_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_resource_id_contact', 'contact', 'resource', ['resource_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_resource_id_country', 'country', 'resource', ['resource_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_resource_id_currency', 'currency', 'resource', ['resource_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_employee_id_employee_contact', 'employee_contact', 'employee', ['employee_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_contact_id_employee_contact', 'employee_contact', 'contact', ['contact_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_employee_id_employee_passport', 'employee_passport', 'employee', ['employee_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_passport_id_employee_passport', 'employee_passport', 'passport', ['passport_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_employee_id_employee_address', 'employee_address', 'employee', ['employee_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_address_id_employee_address', 'employee_address', 'address', ['address_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_resource_id_employee', 'employee', 'resource', ['resource_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_resource_id_foodcat', 'foodcat', 'resource', ['resource_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_resource_id_hotel', 'hotel', 'resource', ['resource_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_hotelcat_id_hotel', 'hotel', 'hotelcat', ['hotelcat_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_location_id_hotel', 'hotel', 'location', ['location_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_resource_id_hotelcat', 'hotelcat', 'resource', ['resource_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_resource_id_licence', 'licence', 'resource', ['resource_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_resource_id_location', 'location', 'resource', ['resource_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_region_id_location', 'location', 'region', ['region_id'], ['id'], onupdate='cascade', ondelete='restrict')
    op.create_foreign_key('fk_resource_id_navigation', 'navigation', 'resource', ['resource_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_navigation_position_id', 'navigation', 'position', ['position_id'], ['id'], onupdate='cascade', ondelete='restrict')
    op.create_foreign_key('fk_parent_id_navigation', 'navigation', 'navigation', ['parent_id'], ['id'], onupdate='cascade', ondelete='restrict')
    op.create_foreign_key('fk_resource_id_passport', 'passport', 'resource', ['resource_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_country_id_passport', 'passport', 'country', ['country_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_resource_type_id_permission', 'permision', 'resource_type', ['resource_type_id'], ['id'], ondelete='cascade', onupdate='cascade')
    op.create_foreign_key('fk_position_id_permision', 'permision', 'position', ['position_id'], ['id'], ondelete='cascade', onupdate='cascade')
    op.create_foreign_key('fk_permision_structure_id', 'permision', 'structure', ['structure_id'], ['id'], onupdate='cascade', ondelete='restrict')
    op.create_foreign_key('fk_person_id_person_contact', 'person_contact', 'person', ['person_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_contact_id_person_contact', 'person_contact', 'contact', ['contact_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_person_id_person_passport', 'person_passport', 'person', ['person_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_passport_id_person_passport', 'person_passport', 'passport', ['passport_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_person_id_person_address', 'person_address', 'person', ['person_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_address_id_person_address', 'person_address', 'address', ['address_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_resource_id_person', 'person', 'resource', ['resource_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_resource_id_position', 'position', 'resource', ['resource_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_position_structure_id', 'position', 'structure', ['structure_id'], ['id'], onupdate='cascade', ondelete='restrict')
    op.create_foreign_key('fk_resource_id_region', 'region', 'resource', ['resource_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_region_country_id', 'region', 'country', ['country_id'], ['id'], onupdate='cascade', ondelete='restrict')
    op.create_foreign_key('fk_resource_id_resource_log', 'resource_log', 'resource', ['resource_id'], ['id'], onupdate='cascade', ondelete='restrict')
    op.create_foreign_key('fk_employee_id_resource_log', 'resource_log', 'employee', ['employee_id'], ['id'], onupdate='cascade', ondelete='restrict')
    op.create_foreign_key('fk_resource_id_resource_type', 'resource_type', 'resource', ['resource_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_resource_type_id_resource', 'resource', 'resource_type', ['resource_type_id'], ['id'], onupdate='cascade', ondelete='restrict')
    op.create_foreign_key('fk_structure_id_resource', 'resource', 'structure', ['structure_id'], ['id'], onupdate='cascade', ondelete='restrict')
    op.create_foreign_key('fk_resource_id_roomcat', 'roomcat', 'resource', ['resource_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_structure_id_structure_contact', 'structure_contact', 'structure', ['structure_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_contact_id_structure_contact', 'structure_contact', 'contact', ['contact_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_structure_id_structure_bank_detail', 'structure_bank_detail', 'structure', ['structure_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_bank_detail_id_structure_bank_detail', 'structure_bank_detail', 'bank_detail', ['bank_detail_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_structure_id_structure_address', 'structure_address', 'structure', ['structure_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_address_id_structure_address', 'structure_address', 'address', ['address_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_resource_id_structure', 'structure', 'resource', ['resource_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_structure_parent_id', 'structure', 'structure', ['parent_id'], ['id'], onupdate='cascade', ondelete='restrict')
    op.create_foreign_key('fk_task_id_task_resource', 'task_resource', 'task', ['task_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_resource_id_task_resource', 'task_resource', 'resource', ['resource_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_resource_id_task', 'task', 'resource', ['resource_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_employee_id_task', 'task', 'employee', ['employee_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_tour_id_tour_point', 'tour_point', 'tour', ['tour_id'], ['id'], ondelete='cascade', onupdate='cascade')
    op.create_foreign_key('fk_location_id_tour_point', 'tour_point', 'location', ['location_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_hotel_id_tour_point', 'tour_point', 'hotel', ['hotel_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_accomodation_id_tour_point', 'tour_point', 'accomodation', ['accomodation_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_foodcat_id_tour_point', 'tour_point', 'foodcat', ['foodcat_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_roomcat_id_tour_point', 'tour_point', 'roomcat', ['roomcat_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_tour_id_tour_person', 'tour_person', 'tour', ['tour_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_person_id_tour_person', 'tour_person', 'person', ['person_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_resource_id_tour', 'tour', 'resource', ['resource_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_touroperator_id_tour', 'tour', 'touroperator', ['touroperator_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_customer_id_tour', 'tour', 'person', ['customer_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_advsource_id_tour', 'tour', 'advsource', ['advsource_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_currency_id_tour', 'tour', 'currency', ['currency_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_start_location_id_tour', 'tour', 'location', ['start_location_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_end_location_id_tour', 'tour', 'location', ['end_location_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_touroperator_id_touroperator_bperson', 'touroperator_bperson', 'touroperator', ['touroperator_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_bperson_id_touroperator_bperson', 'touroperator_bperson', 'bperson', ['bperson_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_touroperator_id_touroperator_licence', 'touroperator_licence', 'touroperator', ['touroperator_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_licence_id_touroperator_licence', 'touroperator_licence', 'licence', ['licence_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_touroperator_id_touroperator_bank_detail', 'touroperator_bank_detail', 'touroperator', ['touroperator_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_bank_detail_id_touroperator_bank_detail', 'touroperator_bank_detail', 'bank_detail', ['bank_detail_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_resource_id_touroperator', 'touroperator', 'resource', ['resource_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_resource_id_user', 'user', 'resource', ['resource_id'], ['id'], ondelete='restrict', onupdate='cascade')
    op.create_foreign_key('fk_employee_id_user', 'user', 'employee', ['employee_id'], ['id'], ondelete='restrict', onupdate='cascade')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('unique_idx_users_username', 'user')
    op.drop_constraint('unique_idx_users_email', 'user')
    op.drop_constraint('unique_idx_name_touroperator', 'touroperator')
    op.drop_constraint('unique_idx_name_roomcat', 'roomcat')
    op.drop_constraint('unique_idx_resource_type_name', 'resource_type')
    op.drop_constraint('unique_idx_resource_type_module', 'resource_type')
    op.drop_constraint('unique_idx_name_country_id_region', 'region')
    op.drop_constraint('unique_idx_name_strcuture_id_position', 'position')
    op.drop_constraint('unique_idx_resource_type_id_position_id_permision', 'permision')
    op.drop_constraint('unique_idx_name_region_id_location', 'location')
    op.drop_constraint('unique_idx_name_hotelcat', 'hotelcat')
    op.drop_constraint('unique_idx_name_foodcat', 'foodcat')
    op.drop_constraint('unique_idx_currency_iso_code', 'currency')
    op.drop_constraint('unique_idx_country_iso_code', 'country')
    op.drop_constraint('unique_idx_name_bank', 'bank')
    op.drop_constraint('unique_idx_name_advsource', 'advsource')
    op.drop_constraint('unique_idx_accomodation_name', 'accomodation')
    ### end Alembic commands ###
