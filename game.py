#coding:utf-8
import pygame
from classe import *
pygame.init()
resolution=(400,400)
clock=pygame.time.Clock()
white=[255,255,255]
pygame.display.set_caption("ma surface")
surface = pygame.display.set_mode(resolution)#Surface
jeu_lance=True
liste_pion=[]
liste=affichage_carro(surface)
liste_pion=affichage_pion(surface)
pygame.display.flip()
double_info=False
rectan_tempo=[]
ma_case=False
can_pass=False
#number=0
finish=False
turn=True
turns_color="white"


        


while jeu_lance:
    #nombre=len(liste_pion)-1
    pygame.display.flip()
    for event in pygame.event.get():

        if event.type==pygame.QUIT:
                jeu_lance=False
        elif event.type == pygame.MOUSEBUTTONUP:
            for pon,e in enumerate(liste_pion):
                if can_pass:
                    if rectan_tempo==[]:
                        can_pass=False
                    else:
                        for a,i in enumerate(rectan_tempo):
                                if i.x<event.pos[0]<i.x+50 and i.y<event.pos[1]<i.y+50:
                                    if num_pion==e.num_pion and e.color==turns_color:
                                            e.move(surface,liste,liste_pion,i)
                                            check=e.question_kill(surface,liste_pion,liste)
                                            rectan_tempo=[]
                                            can_pass=False
                                            
                                            if turn:
                                                turn=False
                                                turns_color="black"
                                            else:
                                                turns_color="white"
                                                turn=True
                                            if type(check)==king:
                                                if check.king_dead:
                                                    finish=True
                                                    if check.color=="black":
                                                        color="white"
                                                    else:
                                                        color="black"

                               
                                elif e.x<event.pos[0]<e.x+50 and e.y<event.pos[1]<e.y+50 and num_pion==e.num_pion:#Reclique sur le meme pion
                                            
                                            can_pass=False
                                            rectan_tempo=[]
                                            for c in liste:
                                                pygame.draw.rect(surface,c.color,c)
                                            for i in liste_pion:
                                                surface.blit(i.pion,[i.case_pion[i.NcaseX],i.case_pion[str(i.NcaseY)]])
                                            double_info=False
                                            can_pass=False
                                            rectan_tempo=[]
                                            


                                
                elif e.x<event.pos[0]<e.x+50 and e.y<event.pos[1]<e.y+50:#clique sur un pion
                        if double_info:
                            for c in liste:
                                pygame.draw.rect(surface,c.color,c)
                            for i in liste_pion:
                                surface.blit(i.pion,[i.case_pion[i.NcaseX],i.case_pion[str(i.NcaseY)]])
                                double_info=False
                                can_pass=False
                                rectan_tempo=[]
                        
                        
                
                        else:
                                        
                            rectan_tempo=e.show_move(surface,liste,liste_pion)
                            indice=len(rectan_tempo)-1
                            can_pass=True
                            num_pion=e.num_pion
                            double_info=True
                        
                
            if finish:
                print(f"les {color} ont gagné")
                jeu_lance=False

                                               
        
            

                                    
    clock.tick(20)
    #print(clock.get_fps())
    pygame.display.flip()
    













    




        























    

        


    
    



       


    


        



        

    
        

        
            
        
    
 

















    

   




