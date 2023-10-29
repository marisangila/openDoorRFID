
from dal.Person_DAL import *
from enu.Access import *

class Authentication_BLL:
    
    __person = Person_DAL('localhost','root','','open_door')
       
    def authenticate_person(pk_person):
        # self.__Person.list_person(pk_person)
        # return person.fk_access == Access.AUTHORIZED
        return Access_Model.AUTHORIZED