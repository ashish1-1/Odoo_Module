import xmlrpc.client
import datetime
url = 'http://192.168.5.90:8017'
db = 'resume_db'
username = 'admin'
password = 'webkul'

# Check Version
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
print(common.version(),"\n\n")

uid = common.authenticate(db, username, password, {})
print(uid)
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

# Create New Record
model_name_1 = "resume.application"

# search data for country id
country_id = models.execute_kw(db, uid, password, "res.country", 'search', [[['name','=','India']]],)


# Search data for state_id
state_id = models.execute_kw(db, uid, password, "res.country.state", 'search', [[['name','=','Uttar Pradesh']]],)



dob = datetime.datetime(1998, 5, 17).strftime("%Y-%m-%dT%H:%M:%S")
new_record = {
    'name':'Ashish Varshney',
    'father_name':'CP Varshney',
    'email':'Ankur@gmail.com',
    'dob':dob,
    'linked_info':'likedin info',
    'job_postion':'Software Developer',
    'introduction':'To seek a role in a company where I can contribute my ideas and be mentored towards a successful career',
    'mobile':'6369857456',
    'street':'H-block Sector-62',
    'city':'Noida',
    'zip':'2100302',
    'country_id':country_id[0],
    'state_id':state_id[0],
}

try:
    new_resume_record_id = models.execute_kw(db,uid,password,model_name_1,'create',[new_record])
    # Create data for Education Qualification
    education_new_record = {
        'board':'CBSE',
        'school_college':'Saraswati vidya mandir Sr. Sec. School',
        'year':'2016',
        'max_marks':'500',
        'marks_obtained':'348',
        'percentage_cgpa':'percentage',
        'degree':'10th',
        'resume_application_id': new_resume_record_id
    }

    new_edu_record_id = models.execute_kw(db,uid,password,"education.background",'create',[education_new_record])


    # Search the record
    # ids = models.execute_kw(db, uid, password, model_name_1, 'search', [[]], {'limit': 5})
    # print(ids)

    # Update an existing record
    # update_record={
    #     'mobile':'0970789118',
    #     'street':'Laxman Puram Colony'
    # }
    # models.execute_kw(db,uid,password,model_name,'write',[ids[1],update_record])

    # # Read the fields of a record
    # record = models.execute_kw(db, uid, password, model_name_1, 'read', [ids[0]],{'fields':model_field})

    # print(record)
    # print(record[0]['name'])
    # print(record[0]['dob'])
    # print(record[0]['mobile'])
    # print(record[0]['street'])
    # print(record[0]['city'])
    # print(record[0]['zip'])

    # Delete existing a record
    # models.execute_kw(db,uid,password,model_name,'unlink',[[ids[1]]])

    # --------------------FOR LEVEL-2 ----------------------

    # records = models.execute_kw(db, uid, password, model_name_1, 'read', [ids])
    # print(records)
    # ================================================================
    # Fetch Skill records

    # skill_records = models.execute_kw(db, uid, password, "resume.skill", 'read', [records[0]['skill_ids']])
    # print(skill_records[0])
    # for key, value in skill_records[0].items():
    #     print(f"{key}=====>{value}")

    # ================================================================
    # Create new skill Records


    skill_type_ids = models.execute_kw(db, uid, password, "hr.skill.type", 'search', [[]], {'limit': 3})

    skill_type_records = models.execute_kw(db, uid, password, "hr.skill.type", 'read', [skill_type_ids[0]])
    # print(skill_type_records)


    skill_ids = models.execute_kw(db, uid, password, "hr.skill", 'search', [[['skill_type_id','=',skill_type_ids[0]]]], {'limit': 3})
    print(skill_ids)


    skill_level_ids = models.execute_kw(db, uid, password, "hr.skill.level", 'search', [[['skill_type_id','=',skill_type_ids[0]]]], {'limit': 5})
    print(skill_level_ids)


    new_skill_record={
        'name':skill_ids[0],
        'skill_type_id': skill_type_ids[0],
        'skill_level_id':skill_level_ids[0],
        'resume_id':new_resume_record_id,
    }
    skill_record_id = models.execute_kw(db,uid,password,'resume.skill','create',[new_skill_record])

    # SEARCH FOR CUSTOM SKILLS
    custom_skill_type_ids = models.execute_kw(db, uid, password, "skill.type", 'search', [[]], {'limit': 3})

    custom_skill_ids = models.execute_kw(db, uid, password, "skill.skills", 'search', [[['skill_type_id','=',custom_skill_type_ids[0]]]], {'limit': 3})

    custom_new_skill_record = {
        'skill_type_id':custom_skill_type_ids[0],
        'skills_id':custom_skill_ids[0],
        'skill_progress':'intermediate',
        'resume_id':new_resume_record_id,
    }


    custom_skill_record_id = models.execute_kw(db,uid,password,'skill.type.skills','create',[custom_new_skill_record])



    # print(skill_record_id)

    # new_education_record = {
    #     'board':"CBSE",
    #     'school_college':'SVM',
    #     'year':"2016",
    #     'max_marks':'500',
    #     'marks_obtained':"376",
    #     "percentage_cgpa":"percentage",
    #     'degree':"10th",
    #     "resume_application_ids":record_id,
    # }
    # edu_record_id = models.execute_kw(db,uid,password,'education.background','create',[new_education_record])
    # print(edu_record_id)

    # # =========================================================
    # # Delete skill records
    # models.execute_kw(db,uid,password,"resume.skill",'unlink',[[skill_record_id]])



    # Create Experience record
    exp_id = models.execute_kw(db, uid, password, "hr.resume.line.type", 'search', [[['name','=','Experience']]],)

    project_id = models.execute_kw(db, uid, password, "hr.resume.line.type", 'search', [[['name','=','Projects']]],)

    experience_project = {
        'name':'Webkul',
        'line_type_id':exp_id[0],
        'job_position':"s/w developer",
        'date_start':datetime.datetime(2023, 3, 17).strftime("%Y-%m-%dT%H:%M:%S"),
        'description':"This is description ",
        'technology_used':"Python",
        'resume_id':new_resume_record_id,
    }

    new_exp_record_id = models.execute_kw(db,uid,password,'experience.project','create',[experience_project])

    experience_project = {
        'name':'Tic Tac Toe Game',
        'line_type_id':project_id[0],
        'job_position':"s/w developer",
        'date_start':datetime.datetime(2023, 3, 17).strftime("%Y-%m-%dT%H:%M:%S"),
        'description':"This is description ",
        'technology_used':"Python",
        'no_of_people_involved':3,
        'resume_id':new_resume_record_id,
    }

    new_pro_record_id = models.execute_kw(db,uid,password,'experience.project','create',[experience_project])

    # Create record for certification and achivements

    certification_data = {
        'name':'Python Data Strtucture (Great Learning)',
        'resume_id':new_resume_record_id
    }

    new_certification_record_id = models.execute_kw(db,uid,password,'certification.certifications','create',[certification_data])

    achivements_data = {
        'name':'4 star on Hackrrank',
        'resume_id':new_resume_record_id
    }

    new_achivements_record_id = models.execute_kw(db,uid,password,'achivement.achivements','create',[achivements_data])

    # create hobbies data
    hobbies_id = models.execute_kw(db, uid, password, "hobbie.hobbies", 'search', [[]],)

    hobbie_record = {
        'hobbies_ids':[(4, hobbie_id) for hobbie_id in hobbies_id]
    }
    new_hobbie_record_id = models.execute_kw(db,uid,password,'resume.application','write',[[new_resume_record_id],hobbie_record] )

    print(new_hobbie_record_id)

except:
    print("Email must be Unique")

