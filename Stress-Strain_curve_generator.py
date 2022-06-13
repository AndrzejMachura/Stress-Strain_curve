"""This script is responsible for generating non-linear Stress-Strain curve usig Ramberg-Osgood relation  
   and linear curve acording to Hooke's law.
   The output of this script are:
   1. Text file containig elasto-plastic and linear defintinion of given material
   2. Chart with drawn Stress-Strain curve of given material.
"""
import pylab
from os import system
import isotropic_material

class MatNameError (Exception):
    pass
class NegativeValue (Exception):
    pass
class ModulusError (Exception):
    pass
class UltStrError (Exception):
    pass
class ElongationError (Exception):
    pass

def generate_chart(Y=isotropic_material.Mat("2024-T72", 470, 300, 11, 71000)):

    ultimate_elongation = [0., 1.1*max(Y.generate_r_o_strain())]
    ultimate_stress = [Y.Ftu, Y.Ftu]

    pylab.title("Stress-Strain")
    pylab.plot(Y.generate_r_o_strain(),Y.generate_stress_list(),'y', Y.generate_true_strain(),Y.generate_true_stress(),'b',ultimate_elongation,ultimate_stress,'r')
    pylab.legend(['Engineering Stress-Strain','True Stress-Strain','Ultimate Stregnth'], loc='lower right', shadow=True, fontsize='medium', title='Legend')
    pylab.ylim(0., 1.1*max(Y.generate_true_stress()))
    pylab.ylabel("Stress [MPa]")
    pylab.xlim(0., 1.1*max(Y.generate_r_o_strain()))
    pylab.xlabel("Strain [-]") 
    pylab.grid(True)  
    pylab.savefig(str(Y.mat_name)+".jpg", dpi = 720) 
    pylab.show()

def generate_text_file(X=isotropic_material.Mat("2024-T72", 470, 300, 11, 71000)):
    file = open(X.mat_name+".txt","w")
    file.write(str(X)+"\n")
    file.write("Row Number\tEngineering Strain\tEngineering Stress\tTrue Strain\tTrue Stress \n")
    i=0
    while i < len(X.generate_stress_list()):
        e_strain = "{:.3e}".format(X.generate_r_o_strain()[i])
        e_stress = "{:.3e}".format(X.generate_stress_list()[i])
        tr_strain = "{:.3e}".format(X.generate_true_strain()[i])
        tr_stress = "{:.3e}".format(X.generate_true_stress()[i])
        file.write(str(i+1)+"\t"+str(e_strain)+"\t"+str(e_stress)+"\t"+str(tr_strain)+"\t"+str(tr_stress)+"\n")
        i+=1
    
    file.close()

print("This script is responsible for generating non-linear Stress-Strain curve usig Ramberg-Osgood relation and linear curve acording to Hooke's law.")
print("Required units are given in brackets \n")

while True:
    print("Menu:\n")
    print("1. Generate new curve")
    print("2. Plot Stress-Strain chart (default:2024-T42)")
    print("3. Generate output file (default 2024-T42)")
    print("4. Exit\n") 
    try: 
        i= int(input("Print number to choose option:\n"))
    except ValueError:
        print("Menu option must be given")
        system("PAUSE")
        print("\n")
        continue

    match i:
        case 1:      
            try:
                mat_name= input("Give material name: ")
                if mat_name =="": raise MatNameError
                E = float (input("Give Younga modulus (MPa): "))
                Ftu = float (input("Give Ultimate Tensile Strength (MPa): "))
                Fty = float (input("Give Yield Tensile Strength (MPa): ")) 
                u = float (input("Give maximum elongation (%): "))
                material = isotropic_material.Mat(mat_name, Ftu, Fty, u, E)
                
                if E<0 or Ftu<0 or Fty<0 or u<0: raise NegativeValue
                if E<Ftu: raise ModulusError
                if Ftu<Fty: raise UltStrError
                if u/100.<= 0.002: raise ElongationError

            except MatNameError:
                print("\n") 
                print("Material should be named.\n")               
                system("PAUSE")
                print("\n")              
                continue

            except ValueError:
                print("\n") 
                print("All marterial physical properties should be given.\n")               
                system("PAUSE")
                print("\n")              
                continue

            except NegativeValue:
                print("\n") 
                print("All marterial physical properties should be positive numbers.\n")
                system("PAUSE")
                print("\n")                 
                continue

            except ModulusError:
                print("\n")                 
                print("Young Modulus should be greater than Ultimate Tensile Strength.\n")
                system("PAUSE")
                print("\n")                  
                continue

            except UltStrError:
                print("\n")                
                print("Ultimate Tensile Strength should be greater than Yield Tensile Strength.\n")
                system("PAUSE")
                print("\n")                
                continue

            except ElongationError:
                print("\n")                
                print('Maximum Elongation should be greater than 0.2%.\n')
                system("PAUSE")
                print("\n")                
                continue                
        case 2:
            try:
                generate_chart(material)
            except NameError:
                generate_chart()
        
        case 3:
            try:
                generate_text_file(material)
            except NameError:
                generate_text_file()
        case 4:
            break