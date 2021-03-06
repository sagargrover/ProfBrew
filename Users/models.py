"""
Author: Amitayush Thakur, Sagar Grover and Abhimanyu Siwach
This file contains various models for our databases.
"""
from django.db import models
from django.utils import timezone
from University.models import College


#Some Important Parameters
MAX_LEN_OF_USERNAME=15
MAX_LEN_OF_NAME=200
MAX_LEN_OF_PASSWORD=30
MAX_LEN_OF_UNIV_NAME=100
MAX_LEN_OF_CLG_NAME=100
MAX_LEN_OF_DEG_NAME=100
MAX_LEN_OF_DIS_NAME=100
MAX_LEN_OF_PROF_QUALIFICATION=200
MAX_LEN_OF_PROF_INTEREST=200
MAX_LEN_OF_PROF_COURSES=200
DEFAULT_FIELD_VALUE=None
DEFAULT_NUMBER_OF_QUALIFICATIONS=1

class Qualification_Type(models.Model):
    qualification_name = models.CharField(max_length=MAX_LEN_OF_PROF_QUALIFICATION,default=DEFAULT_FIELD_VALUE)
    def __str__(self):
        return self.qualification_name
    
class Prof_Position(models.Model):
    priority=models.BigIntegerField(null=True)
    position_name = models.CharField(max_length=MAX_LEN_OF_DEG_NAME,default=DEFAULT_FIELD_VALUE)
    def __str__(self):
        return self.position_name
    
class Prof_Qualifications(models.Model):
    number_of_qualifications = models.IntegerField(null=False,default=DEFAULT_NUMBER_OF_QUALIFICATIONS)
    qualifications=models.ManyToManyField(Qualification_Type)
    def __str__(self):
        return str(self.number_of_qualifications)

class Users(models.Model):
    """
        Users()- Extends Django's pre-implimented User class. 
        The User class is meant for storing the details of the users into database and keep track of the users.
            _username -> private field and is the primary key.
            name -> has the name of the person. It is public.
            _password -> private and encrypted.
            _email -> private field and has valid email address.
            user_type -> has the user type and is public.
            _mobile_number -> private and is the only optional field
    """
    STUDENT=1
    PROFESSOR=2
    VISITOR=3
    USER_TYPE = ((STUDENT,'Student'),(PROFESSOR,'Professor'),(VISITOR,'Visitor'),)
    _username = models.CharField(primary_key=True,max_length=MAX_LEN_OF_USERNAME,null=False,default=DEFAULT_FIELD_VALUE)  #Primary Key
    name = models.CharField(max_length=MAX_LEN_OF_NAME,null=False,default=DEFAULT_FIELD_VALUE)
    _password = models.CharField(max_length=MAX_LEN_OF_PASSWORD,null=False,default=DEFAULT_FIELD_VALUE)
    user_type = models.IntegerField(choices=USER_TYPE,default=VISITOR,null=False)
    _email = models.EmailField(null=False,default=DEFAULT_FIELD_VALUE)
    _mobile_number = models.BigIntegerField(null=True)  #Optional Field
    _date_joined = models.DateTimeField(null=False,default=timezone.now())
    def __str__(self):
        """ __str__()- returns the name of the user """
        return self.name
    def get_email(self):
        return self.email
    def get_mobile_number(self):
        return self.mobile_number
    def get_name(self):
        return self.name
    def get_user_type(self):
        return self.user_type
    def get_username(self):
        return self.username
    def get_join_date_time(self):
        return self.date_joined
    def update_name(self,name):
        self.name=name
    def update_username(self,username):
        self.username=username
    def update_password(self,password):
        self.password=password
    def update_email(self,email):
        self.email=email
    def update_mobile_number(self,number):
        self.mobile_number=number
    def update_type(self,user_type):
        self.user_type=user_type
    class Meta:
        abstract=True;
        
class Student(Users):
    """
        Student()- Extends Users(). It represents the student community.
        The database has some new fields like credibility which depends on how much student 
        contributes in ratings.
        We can add a fields like "Discipline" and "Degree Being Pursued"  
            _conributing_factor -> is the measure of student's contribution in updating website info.
                                   It is calculated using a an algorithm.
            _degree_persued -> is the name of the degree being pursued by the student.
                               *Suggestion: Change it to Enum
            _discipline -> is the name of the discipline of the student.
    """
    _contributing_factor = models.BigIntegerField(null=False,default=DEFAULT_FIELD_VALUE)
    _college = models.ForeignKey(College,default=DEFAULT_FIELD_VALUE,blank=False)      #Is a foreign key
    _degree_pursued = models.CharField(max_length=MAX_LEN_OF_DEG_NAME,null=False,default=DEFAULT_FIELD_VALUE)
    _discipline = models.CharField(max_length=MAX_LEN_OF_DIS_NAME,null=False,default=DEFAULT_FIELD_VALUE)
    def get_contributing_factor(self):
        return self._contributing_factor
    def get_university(self):
        return self.unversity
    def get_college(self):
        return self._college
    def update_contributing_factor(self,contributing_factor):
        self._contributing_factor=contributing_factor
    def update_university(self,university):
        self._college.update_university(university)
    def update_college(self,college):
        self._college=college
      
class Professor(Users):
    """
        Professor()- Extends Users(). It represents the professors of various colleges.
        The database has some new fields like ratings which depends on the overall performance of the 
        professor and the way he is rated by the students of the respective college.
            _ratings -> has the compact rating of the professor
    """
    _ratings = models.BigIntegerField(null=False,default=DEFAULT_FIELD_VALUE)
    _college = models.ForeignKey(College,default=DEFAULT_FIELD_VALUE,blank=False)  #Is a Foreign Key
    _qualifications = models.ForeignKey(Prof_Qualifications)
    _area_of_interest = models.CharField(max_length=MAX_LEN_OF_PROF_INTEREST,null=False,default=DEFAULT_FIELD_VALUE)
    _courses_teaching = models.CharField(max_length=MAX_LEN_OF_PROF_COURSES,null=False,default=DEFAULT_FIELD_VALUE)
    _best_known_for = models.CharField(max_length=MAX_LEN_OF_PROF_COURSES,null=False,default=DEFAULT_FIELD_VALUE)
    _popular_name = models.CharField(max_length=MAX_LEN_OF_NAME,null=False,default=DEFAULT_FIELD_VALUE)
    _position=models.ManyToManyField(Prof_Position)
    def get_university(self):
        return self._unversity
    def get_college(self):
        return self._college
    def get_popular_name(self):
        return self._popular_name
    def get_area_of_interest(self):
        return self._area_of_interest
    def get_courses_teaching(self):
        return self._courses_teaching
    def get_best_known_for(self):
        return self._best_known_for
    def get_ratings(self):
        return self._raitngs
    def get_qualifications(self):
        return self._qualifications
    def get_position(self):
        return self._position
    def update_position(self,position):
        self._position=position
    def update_qualifications(self,qualifications):
        self._qualifications=qualifications
    def upadate_college(self,college):
        self._college=college
    def update_area_of_interest(self,interest):
        self._area_of_interest=interest
    def update_best_known_for(self,known_for):
        self._best_known_for=known_for
    def update_courses_teaching(self,courses):
        self._courses_teaching=courses
    def update_popular_name(self,name):
        self._popular_name=name
    def update_university(self,university):
        self._college.update_university(university)
    def update_ratings(self,ratings):
        self._ratings=ratings
