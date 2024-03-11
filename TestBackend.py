import vpython as vp
import numpy as np
#=================================================================
# region method overloads for convenions
def arrow(**kid):
    return vp.arrow(pos = kid["pos"], axis = kid["axis"], round = True)

def vec(x,y,z):
    return vp.vec(x,y,z)

def sphere(**kid):
    return vp.sphere(pos = kid["pos"], radius = 0.1, make_trail = False, color = 1/255 * vec(255,150,0))

def radians(number):
    return vp.radians(number)

def sin(number):
    return vp.sin(number)

def cos(number):
    return vp.cos(number)

def arange(min, max, change):
    return vp.arange(min, max, change)

def cylinder(**kid):
    return vp.cylinder(pos = kid["pos"], axis = kid["axis"], radius = 0.1) #, color = kid["color"])

def pi():
    return vp.pi

def ring(**kid):
    return vp.ring(pos = kid["pos"], axis = kid["axis"], radius = kid["radius"])

def rate(number):
    return vp.rate(number)

def cross(number_1, number_2):
    return vp.cross(number_1, number_2)

def mag(number):
    return vp.mag(number)

def hat(number):
    return vp.hat(number)

def sqrt(number):
    return vp.sqrt(number)
# endregion
#=================================================================

class GraphicsTools():
    number_of_nodes = 0
    number_of_current_members = 0
    number_of_equations = 0

    list_of_nodes = [] # Will contain all nodes, examples 3 nodes
    list_of_spheres = []
    list_of_labels = []
    list_of_force = []
    list_of_angle = []
    list_of_force_arrows = []
    
    list_of_elements = [] # Will contain all the elements, connections between nodes, also the number of unknowns
    list_of_elements_label = []
    element_visual_list = [] # will hold something
    list_of_unknowns = [] # based on the amount of memebers

    def __init__(self): # The constructor for this class that will always be called when first created
        # region Gobal Coordiante System 
        origin = vec(0, 0, 0)
        axis = vp.sphere(pos = origin, radius = 10)  # Here radius is length of axis
        axis.l = axis.radius  # Lenght of axis arrows
        axis.s = axis.radius/100         # Radius of axis arrows, so if lenght is 5 then radius is 0.05
        axis.f = 'monospace'
        axis.toffset = 0.05
        axis.visible = False
        op = 0.5

        pos_x_axis = arrow(pos = origin, axis = vec(axis.l, 0, 0))
        pos_x_axis.shaftwidth = axis.s
        pos_x_axis.color = vec(1, 0, 0)
        pos_x_axis.opacity = op

        pos_x_axis_label = vp.label(pos = pos_x_axis.pos + pos_x_axis.axis + vec(axis.toffset, 0, 0), 
                text='+x', height = 16, border = 4, font = axis.f, line = False, opacity = 0, box = False)
                
        neg_x_axis = arrow(pos = origin, axis = vec(-axis.l, 0, 0))
        neg_x_axis.shaftwidth = axis.s
        neg_x_axis.color = vec(1, 0, 0)
        neg_x_axis.opacity = op

        neg_x_axis_label = vp.label(pos = neg_x_axis.pos + neg_x_axis.axis + vec(-axis.toffset, 0, 0), 
                text='-x', height = 16, border = 4, font = axis.f, line = False, opacity = 0, box = False)
                
        pos_y_axis = arrow(pos = origin, axis = vec(0, axis.l, 0))
        pos_y_axis.shaftwidth = axis.s 
        pos_y_axis.color = vec(0, 1, 0)
        pos_y_axis.opacity = op

        pos_y_axis_label = vp.label(pos = pos_y_axis.pos + pos_y_axis.axis + vec(0, axis.toffset, 0), 
                text='+y', height = 16, border = 4, font = axis.f, line = False, opacity = 0, box = False)
                
        neg_y_axis = arrow(pos = origin, axis = vec(0, -axis.l, 0))
        neg_y_axis.shaftwidth = axis.s
        neg_y_axis.color = vec(0, 1, 0)
        neg_y_axis.opacity = op

        neg_y_axis_label = vp.label(pos = neg_y_axis.pos + neg_y_axis.axis + vec(0, -axis.toffset, 0), 
                text='-y', height = 16, border = 4,font = axis.f, line = False, opacity = 0, box = False)

        # pos_z_axis = arrow(pos = origin, axis = vec(0,0,axis.l))
        # pos_z_axis.shaftwidth = axis.s
        # pos_z_axis.color = vec(0, 0, 1)
        # pos_z_axis.opacity = op

        # pos_z_axis_label = vp.label(pos = pos_z_axis.pos + pos_z_axis.axis + vec(0, axis.toffset, 0), 
        #         text='+z', height = 16, border = 4, font = axis.f, line = False, opacity = 0, box = False)
                
        # neg_z_axis = arrow(pos = origin, axis = vec(0,0,-axis.l))
        # neg_z_axis.shaftwidth = axis.s
        # neg_z_axis.color = vp.vec(0, 0, 1)
        # neg_z_axis.opacity = op

        #neg_z_axis_label = vp.label(pos = neg_z_axis.pos + neg_z_axis.axis + vec(0, -axis.toffset, 0), 
        #        text='-z', height = 16, border = 4,font = axis.f, line = False, opacity = 0, box = False)
        #=================================================================
        # endregion
        
    def Bprint(self):
        print("the ref has passed correctly")
        
    # intended to handle new nodes and existing nodes no forces, both cases work
    def node_creation(self, x, y, current_node): # ex if current node is five thn we expect a label of five
        print(f"number of nodes backend {self.number_of_nodes} vs current number {current_node}")
        
        # what if a number was skipped? then how to assign label
        
        if current_node > self.number_of_nodes and current_node - 1 == self.number_of_nodes: # so doesn't exit in list of nodes
            self.list_of_spheres.append(sphere(pos = vec(x, y, 0))) # create sphere and label
            # creates label for current if current is new head of pack 
            self.list_of_labels.append(vp.label(pos = vec(x, y, 0), text = f"{current_node}", xoffset = 5, yoffset = 10, space = 1, 
                    height = 16, border = 4, font = 'monospace', box = False, opacity = 0, color = 1/255 * vec(255,150,0)))
            self.list_of_nodes.append(vec(x, y, 0)) # basically only holds a nodes position, first will be zero
        
            self.number_of_nodes += 1
            print("node created successfully-")
        
        elif current_node > self.number_of_nodes and current_node - 1 != self.number_of_nodes:
            # then we are skipping a few nodes in the line and need to actualize the skipped
            print("Trying to actualize a node without actualizing the preiouvs node ")
            
            number_need_to_actualize = (current_node - 1) - self.number_of_nodes
            
            # now all skipped nodes are tarnsparent
            for x_dalta in range(number_need_to_actualize):
                
                # the objects for the skipped nodes will be created but made transparent
                temp_sphere = sphere(pos = vec(0,0,0))
                temp_sphere.opacity = 0
                
                temp_label = vp.label(pos = vec(0, 0, 0), text = f"{self.number_of_nodes + 1}", xoffset = 5, yoffset = 10, space = 1, 
                        height = 16, border = 4, font = 'monospace', box = False, opacity = 0, color = 1/255 * vec(255,150,0))
                temp_label.visible = False
                
                self.list_of_spheres.append(temp_sphere) # create sphere and label 
                self.list_of_labels.append(temp_label)
                self.list_of_nodes.append(vec(0, 0, 0)) # basically only holds a nodes position, first will be zero
                                
                self.list_of_force.append(0) # leave a placeholder in the list for the node's force
                self.list_of_angle.append(0) # leave a placeholder in the list for the node's angle
                            
                self.list_of_force_arrows.append(vp.arrow(pos = vec(0,0,0), axis = vec(0,0,0), color = 1/255 * vec(236, 215, 16), opacity = 0))
          
                self.number_of_nodes += 1
                print(f"Skipped node {self.number_of_nodes} created successfully")
            
            self.list_of_spheres.append(sphere(pos = vec(x, y, 0))) # create sphere and label 
            self.list_of_labels.append(vp.label(pos = vec(x, y, 0), text = f"{current_node}", xoffset = 5, yoffset = 10, space = 1, 
                    height = 16, border = 4, font = 'monospace', box = False, opacity = 0, color = 1/255 * vec(255,150,0)))
            self.list_of_nodes.append(vec(x, y, 0)) # basically only holds a nodes position, first will be zero
        
            self.number_of_nodes += 1
            print("node created successfully-")
        
        else: # update the sphere and label location
            self.list_of_nodes[current_node - 1] = vec(x, y, 0) # update position data
            self.list_of_labels[current_node - 1].pos = vec(x, y, 0) # update position of label
            self.list_of_spheres[current_node - 1].pos = vec(x, y, 0) # update position of sphere
            
            # if a skipped node then make its objects opacqic
            self.list_of_labels[current_node - 1].visible = True 
            self.list_of_spheres[current_node - 1].opacity = 1 
                      
            print("node updated successfully-")
        
        self.list_of_force.append(0) # leave a placeholder in the list for the node's force
        self.list_of_angle.append(0) # leave a placeholder in the list for the node's angle
        
        self.list_of_force_arrows.append(vp.arrow(pos = vec(0,0,0,), axis = vec(0,0,0), color = 1/255 * vec(236, 215, 16), opacity = 0))
        
        #print(self.list_of_nodes) # good for checking backup list nodes
        return vec(x, y, 0) # a return is not really needed atm but keeping in case
    
    # to handle new nodes and existing node, with new or existing with forces, the case where you have a new node but existing force doesn't exist
    def node_creation_with_force(self, x, y, number_of_node, force, angle):
        print(f"nummmm {number_of_node}")
        
        # we can remove  this line and so we can create a new node with default location and a force
        print(f"so list of nodes only has {len(self.list_of_nodes)} but we are looking for 2")
        #print(f"Backup Node position is <{self.list_of_nodes[number_of_node - 1]}>")
        print("made it passed here")
        if number_of_node > self.number_of_nodes: # so doesn't exit in list of nodes
            self.node_creation(x, y, number_of_node)
            self.force_creation(number_of_node, force, angle) # this requires a node to exist first, the force existing doesn't matter
            # so new node with new force, use this one when enabling the sym from the forces
            print("New baby node has been born")
            
        else: # existing node (MOST OF THE TIME but now adding a force) maybe no position changed or yes, update the sphere and label location or/and updating forces loaction
            print("helloe there")
            # if same position
            if self.list_of_nodes[number_of_node - 1] == vec(x, y, 0):
                print(f"{self.list_of_nodes[number_of_node - 1]} number in list of nodes vs {vec(x,y,0)}")               
                # if force does not exist, then replace the placeholder zeroes with actual arrow
                if self.list_of_force[number_of_node - 1] == 0 and self.list_of_angle[number_of_node - 1] == 0:
                    print("SAME POSITION AND CREATE FORCE")
                    self.force_creation(number_of_node, force, angle)
                
                # if same force, then do nothing
                elif self.list_of_force[number_of_node - 1] == force and self.list_of_angle[number_of_node - 1] == angle:
                     print("SAME POSITOIN AND SAME FORCE")
                     print("nothing changes here")
                
                 # if diff force, just update force with new angles and stuff
                elif self.list_of_force[number_of_node - 1] != force or self.list_of_angle[number_of_node - 1] != angle:
                    print("SAME POSITION BUT REFRESHED FORCE")
                    self.force_creation_E(number_of_node, force, angle)                
                else:
                    print("cry")
           
            else: # if diff position 
                print("skipppp")
                self.list_of_nodes[number_of_node - 1] = vec(x, y, 0) # update position data, might need to do more
            
                self.list_of_labels[number_of_node - 1].pos = vec(x, y, 0) # update position of label
            
                self.list_of_spheres[number_of_node - 1].pos = vec(x, y, 0) # update position of sphere
                
                # if force does not exist, then replace the placeholder zeroes with actual arrow
                if self.list_of_force[number_of_node - 1] == 0 and self.list_of_angle[number_of_node - 1] == 0:
                    print("NEW FORCE CREATE WHILE DIFF POSITION")
                    self.force_creation(number_of_node, force, angle) # hmmmm
                
                # if same force, then do nothing
                elif self.list_of_force[number_of_node - 1] == force and self.list_of_angle[number_of_node - 1] == angle:
                     print("DIFF POSITION BUT SAME FORCE")
                     self.force_creation_E(number_of_node, force, angle)
                
                 # if diff force, just update force with new angles and stuff
                elif self.list_of_force[number_of_node - 1] != force or self.list_of_angle[number_of_node - 1] != angle:
                    self.force_creation_E(number_of_node, force, angle)
                    print("HEY FORCE WAS REFRESHED with NEW POSITION")
                
                else:
                    print("cry again")
                    print(f" current force {self.list_of_force[number_of_node - 1]} and {self.list_of_angle[number_of_node - 1]}")
                    print(f" input force {force} and angle {angle}")

        return vec(x, y, 0)
    
    # create a new 
    def force_creation(self, node_on_which_current_force_acts, force_applied, angles):
        node_location = self.list_of_nodes[node_on_which_current_force_acts - 1]
        print(f"where it gets {node_location}")
        self.list_of_force[node_on_which_current_force_acts - 1] = force_applied
        self.list_of_angle[node_on_which_current_force_acts - 1] = angles
        
        angle = radians(angles)

        force_x = force_applied * cos(angle)
        if abs(force_x) < 0.1000:
            force_x = 0
        
        force_y = force_applied * sin(angle)
        if abs(force_y) < 0.1000:
            force_y = 0
        
        position = vec(force_x, force_y, 0)
        
        offset_from_tail = node_location + hat(position)
        
        self.list_of_force_arrows[node_on_which_current_force_acts - 1].opacity = 0.75 # reveal the force arrow 
        self.list_of_force_arrows[node_on_which_current_force_acts -1].pos = offset_from_tail
        self.list_of_force_arrows[node_on_which_current_force_acts -1].axis = node_location - offset_from_tail
        
        print(f"current number of force arrows is {len(self.list_of_force_arrows)} with the number of nodes being {len(self.list_of_angle)}, they should prob be the sname")
        
        return position

    # just update the force position no change to the force itself
    def force_creation_E(self, node_on_which_current_force_acts, force_applied, angles):
        print(f"passed force {force_applied} and angle {angles} ")
        
        node_location = self.list_of_nodes[node_on_which_current_force_acts - 1]
        print(f"New updated position in backup list is {node_location}")
        
        print("passes here")
        self.list_of_force[node_on_which_current_force_acts - 1] = force_applied
        self.list_of_angle[node_on_which_current_force_acts - 1] = angles
        
        angle = radians(angles)

        force_x = force_applied * cos(angle)
        if abs(force_x) < 0.1000:
            force_x = 0
        
        force_y = force_applied * sin(angle)
        if abs(force_y) < 0.1000:
            force_y = 0
        
        position = vec(force_x, force_y, 0)
        
        offset_from_tail = node_location + hat(position)
        
        print("passed again")
        self.list_of_force_arrows[node_on_which_current_force_acts -1].pos = offset_from_tail
        print("passed a third time")
        self.list_of_force_arrows[node_on_which_current_force_acts -1].axis = node_location - offset_from_tail
        
        print("Something happened.....")
        return position
    
    def calculate_number_of_equations(self): # Needed for correct matrix position
        self.number_of_equations = 2 * self.number_of_nodes # Total number of equations based on number of nodes, now 3 nodes, assume clean data
        print(f"Total number of equations are {self.number_of_equations}")
        
    def element_check(self,current_element, node_number_1, node_number_2):
        print(f"{self.number_of_current_members} element(s) in backend vs current element {current_element}")
        
        # Check to see if completely new element has to be created with no element skips
        if current_element > self.number_of_current_members and current_element - 1 == self.number_of_current_members: 
            print(f"Creating element {current_element}")
            self.element_creation(node_number_1, node_number_2) # if so then just create the element
        
        # Here we are skipping a few elements in the line to create the new element, so we need to actualize the skipped
        elif current_element > self.number_of_current_members and current_element - 1 != self.number_of_current_members:
            print("Trying to actualize an element without actualizing the previous element(s)")
            
            number_need_to_actualize = (current_element - 1) - self.number_of_current_members # math was done to figure out number
            
            # All skipped elements will be create as transparent dumby placeholders
            for x_dalta in range(number_need_to_actualize):
                print(f"Creating skipped element {self.number_of_current_members + 1}")
            
                # for dumby element just default to picking the first two nodes in the list
                self.element_creation(1,2) # if the first two nodes don't exist then think of something else
                
                # then change the opacity of these dumby elements
                self.element_visual_list[self.number_of_current_members - 1].opacity = 0
                self.list_of_elements_label[self.number_of_current_members - 1].visible = False
            
            # Now created desired element  
            print(f"Creating element {current_element}")  
            self.element_creation(node_number_1, node_number_2)
            print("Complex operation conducted successfully")
        
        # Just update the element with new nodes 
        else:
            print("Updating element")
            self.element_update(current_element, node_number_1, node_number_2)
        
        print("Element creation ended-")
        
    def element_creation(self, node_number_1, node_number_2): # Method to connect the two choosen nodes and generates Force vector for the element        

        # Check to flip the inputs
        if node_number_1 > node_number_2:
            temp_number = node_number_2
            node_number_2 = node_number_1
            node_number_1 = temp_number
        
        # Get the nodes (basicaly positions) from the nodes list 
        node_temp_n = self.list_of_nodes[node_number_1 - 1] # The first element of the nodes list
        node_temp_p = self.list_of_nodes[node_number_2 - 1] # The second element of the nodes list

        print(f"node {node_number_1} has loaction {node_temp_n}\n"
              + f"node {node_number_2} has location {node_temp_p}")
        
        # Create visual of element
        element_AB_visual = cylinder(pos = node_temp_n, axis = node_temp_p - node_temp_n)
        element_AB_visual.texture = vp.textures.metal
        
        temp_label = vp.label(pos = 1/2 * (element_AB_visual.axis) + element_AB_visual.pos, 
                text = f"<b>{self.number_of_current_members + 1}</b>", xoffset = 0, yoffset = 0, space = 0, height = 15, 
                border = 1, font = 'monospace', box = True, opacity = 0, linecolor = vec(0,0,0), 
                color = 1/255 * vec(255, 0, 125))
        
        self.list_of_elements_label.append(temp_label)
        self.element_visual_list.append(element_AB_visual)
        self.list_of_unknowns.append(self.number_of_current_members) # Gets number of forces aka memebers
        
        x = node_temp_p.x - node_temp_n.x # As a vector component x
        y = node_temp_p.y - node_temp_n.y # As a vector component y
        c = sqrt(x**2 + y**2)   # Mag of triangle

        element_AB = np.zeros( (self.number_of_equations, 1) ) # Creates an empty matrix where num of eqs is the number of rows, 1 is colum

        # Since node n and node p were choosen then in the element np, the force applied there
        element_AB[node_number_1 * 2 - 2][0] = x/c # The x transformion for the force on the element AB from A
        element_AB[node_number_1 * 2 - 1][0] = y/c # The y transformion for the force on the element AB from A
        element_AB[node_number_2 * 2 - 2][0] = -1 * x/c # The x transformion for the force on the element AB from B
        element_AB[node_number_2 * 2 - 1][0] = -1 * y/c # The y transformion for the force on the element AB from B

        self.list_of_elements.append(element_AB) # holds column matrix

        self.number_of_current_members += 1
        
        print(f"Successfully created element {self.number_of_current_members}")
        print("------------")
        
    def element_update(self, current_element, node_number_1, node_number_2): # Method to connect the two choosen nodes and generates Force vector for the element        

        # Check to flip the inputs
        if node_number_1 > node_number_2:
            temp_number = node_number_2
            node_number_2 = node_number_1
            node_number_1 = temp_number
        
        # Get the nodes (basicaly positions) from the nodes list 
        node_temp_n = self.list_of_nodes[node_number_1 - 1] # The first element of the nodes list
        node_temp_p = self.list_of_nodes[node_number_2 - 1] # The second element of the nodes list

        print(f"node {node_number_1} has loaction {node_temp_n}\n"
              + f"node {node_number_2} has location {node_temp_p}")
        
        # Update visual of element       
        b = self.element_visual_list[current_element - 1].pos = node_temp_n
        a = self.element_visual_list[current_element - 1].axis = node_temp_p - node_temp_n
        self.element_visual_list[current_element - 1].opacity = 1
        
        self.list_of_elements_label[current_element - 1].pos = 1/2 * a + b
        self.list_of_elements_label[current_element - 1].visible = True # useful
        
        x = node_temp_p.x - node_temp_n.x # As a vector component x
        y = node_temp_p.y - node_temp_n.y # As a vector component y
        c = sqrt(x**2 + y**2)   # Mag of triangle

        element_AB = np.zeros( (self.number_of_equations, 1) ) # Creates an empty matrix where num of eqs is the number of rows, 1 is colum

        # Since node n and node p were choosen then in the element np, the force applied there
        element_AB[node_number_1 * 2 - 2][0] = x/c # The x transformion for the force on the element AB from A
        element_AB[node_number_1 * 2 - 1][0] = y/c # The y transformion for the force on the element AB from A
        element_AB[node_number_2 * 2 - 2][0] = -1 * x/c # The x transformion for the force on the element AB from B
        element_AB[node_number_2 * 2 - 1][0] = -1 * y/c # The y transformion for the force on the element AB from B

        # needs more testing 
        self.list_of_elements[current_element - 1] = element_AB # holds column matrix, replaces previous 
        
        print(f"Updated member {self.number_of_current_members} successfully")
    
    def create_matrix(self):
        # After all nodes are created this the next thing calculated
        self.number_of_equations = 2 * self.number_of_nodes # Total number of equations based on number of nodes, now 3 nodes, assume clean data