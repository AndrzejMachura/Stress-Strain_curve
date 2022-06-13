"""This script is responsible for generating non-linear Stress-Strain curve usig Ramberg-Osgood relation  
   and linear curve acording to Hooke's law.
   The output of this script are:
   1. Text file containig elasto-plastic and linear defintinion of given material
   2. Chart with drawn Stress-Strain curve of given material.
"""
import pylab
import isotropic_material

def generate_chart(Y):

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

def generate_text_file(X):
    file = open(X.mat_name+".txt","w")
    file.write(str(X)+"\n")
    file.write("Row Number\tEngineering Strain\tEngineering Stress\tTrue Strain\tTrue Stress \n")
    i=0
    while i < len(material.generate_stress_list()):
        e_strain = "{:.3e}".format(material.generate_r_o_strain()[i])
        e_stress = "{:.3e}".format(material.generate_stress_list()[i])
        tr_strain = "{:.3e}".format(material.generate_true_strain()[i])
        tr_stress = "{:.3e}".format(material.generate_true_stress()[i])
        file.write(str(i+1)+"\t"+str(e_strain)+"\t"+str(e_stress)+"\t"+str(tr_strain)+"\t"+str(tr_stress)+"\n")
        i+=1
    
    file.close()

print("This script is responsible for generating non-linear Stress-Strain curve usig Ramberg-Osgood relation and linear curve acording to Hooke's law.")
print("Required units are given in brackets \n")
# material properties loading

mat_name= input("Give material name: ")
E = float (input("Give Younga modulus (MPa): "))
Ftu = float (input("Give Ultimate Tensile Strength (MPa): "))
Fty = float (input("Give Yield Tensile Strength (MPa): ")) 
u = float (input("Give maximum elongation (%): "))

#create matrial object, generate stress-strain chart, create otput file
material = isotropic_material.Mat(mat_name, Ftu, Fty, u, E)
generate_chart(material)
generate_text_file(material)