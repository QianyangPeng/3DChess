#-*- coding:gbk -*-
m
import main
import pygame
from pygame.locals import *
import sys
from OpenGLLibrary import *
from support import *

pygame.init()

Screen = (1000,600)
Window = glLibWindow(Screen,caption="Chinese Chess")
#Window.toggle_fullscreen()
Chessport = glLibView3D((0,0,Screen[0],Screen[1]),45)
Chessport.set_view()

glLibTexturing(True)

Camera = glLibCamera([0.0,12.0,1.0],[0.0,0.0,0.0])

glLibLighting(True)
Sun1 = glLibLight([0,9,0],Camera)
Sun1.enable()
Sun2 = glLibLight([10,0,0],Camera)
Sun2.enable()
Sun3 = glLibLight([-10,0,0],Camera)
Sun3.enable()
Sun4 = glLibLight([0,14,0],Camera)
Sun4.enable()

Texture = []
Texture.append(glLibTexture("static/qipan.gif"))
Texture.append(glLibTexture("static/hongshuai.gif"))
Texture.append(glLibTexture("static/hongju.gif"))
Texture.append(glLibTexture("static/hongma.gif"))
Texture.append(glLibTexture("static/hongpao.gif"))
Texture.append(glLibTexture("static/hongshi.gif"))
Texture.append(glLibTexture("static/hongxiang.gif"))
Texture.append(glLibTexture("static/hongbing.gif"))
Texture.append(glLibTexture("static/heijiang.gif"))
Texture.append(glLibTexture("static/heiju.gif"))
Texture.append(glLibTexture("static/heima.gif"))
Texture.append(glLibTexture("static/heipao.gif"))
Texture.append(glLibTexture("static/heishi.gif"))
Texture.append(glLibTexture("static/heixiang.gif"))
Texture.append(glLibTexture("static/heizu.gif"))
Texture.append(glLibTexture("static/muban.gif"))
Texture.append(glLibTexture("static/choose.gif"))
Texture.append(glLibTexture("static/slide_left.gif"))
Texture.append(glLibTexture("static/slide_right.gif"))
Texture.append(glLibTexture("static/tmptitle.gif"))
Texture.append(glLibTexture("static/instruction.gif"))
Texture.append(glLibTexture("static/restart.gif"))
Texture.append(glLibTexture("static/save.gif"))
Texture.append(glLibTexture("static/load.gif"))
Texture.append(glLibTexture("static/regret.gif"))
Texture.append(glLibTexture("static/chosen.gif"))
Texture.append(glLibTexture("static/instruction_board.gif"))
Texture.append(glLibTexture("static/cloth.gif"))

Font = pygame.font.Font(os.path.join("fonts","simsun.ttf"),144)

def GetCoordX(cx):
    return -1.8566447177494474+0.46*(cx-1)


def GetCoordY(cy):
    return 2.0948866011315372-0.46*(cy-1)


def GetMessX(x):
    return (x+1.8566447177494474)/0.46+1


def GetMessY(y):
    return (y-2.0948866011315372)/-0.46+1


def Init():
    Chess_ls = getLocalfiles()
    global Texture
    global Objects
    global Objects_pos
    #Objects = [glLibObjTexCube((4.5,0.1,5.0)),glLibObjTexCylinder(0.2,0.1,64),glLibObjTexDisk(0,0.2,64),glLibObjTexCube((0.4,0.01,0.4))]

    Objects = []
    Objects_pos = []

    chessboard = glLibObjTexCube((4.5,0.1,5.0))
    Objects.append(chessboard)
    Objects_pos.append([0,0,0])
    #hongshuai
    hongshuai_a = glLibObjTexCylinder(0.2,0.1,64)
    hongshuai_b = glLibObjTexDisk(0,0.2,64)
    Objects.append((hongshuai_a,hongshuai_b))
    Objects_pos.append([GetCoordX(5),0.15,GetCoordY(1)])
    #hongju_left
    hongju_left_a = glLibObjTexCylinder(0.2,0.1,64)
    hongju_left_b = glLibObjTexDisk(0,0.2,64)
    Objects.append((hongju_left_a,hongju_left_b))
    Objects_pos.append([GetCoordX(1),0.15,GetCoordY(1)])
    #hongju_right
    hongju_right_a = glLibObjTexCylinder(0.2,0.1,64)
    hongju_right_b = glLibObjTexDisk(0,0.2,64)
    Objects.append((hongju_right_a,hongju_right_b))
    Objects_pos.append([GetCoordX(9),0.15,GetCoordY(1)])
    #hongma_left
    hongma_left_a = glLibObjTexCylinder(0.2,0.1,64)
    hongma_left_b = glLibObjTexDisk(0,0.2,64)
    Objects.append((hongma_left_a,hongma_left_b))
    Objects_pos.append([GetCoordX(2),0.15,GetCoordY(1)])
    #hongma_right
    hongma_right_a = glLibObjTexCylinder(0.2,0.1,64)
    hongma_right_b = glLibObjTexDisk(0,0.2,64)
    Objects.append((hongma_right_a,hongma_right_b))
    Objects_pos.append([GetCoordX(8),0.15,GetCoordY(1)])
    #hongpao_left
    hongpao_left_a = glLibObjTexCylinder(0.2,0.1,64)
    hongpao_left_b = glLibObjTexDisk(0,0.2,64)
    Objects.append((hongpao_left_a,hongpao_left_b))
    Objects_pos.append([GetCoordX(2),0.15,GetCoordY(3)])
    #hongpao_right
    hongpao_right_a = glLibObjTexCylinder(0.2,0.1,64)
    hongpao_right_b = glLibObjTexDisk(0,0.2,64)
    Objects.append((hongpao_right_a,hongpao_right_b))
    Objects_pos.append([GetCoordX(8),0.15,GetCoordY(3)])
    #hongshi_left
    hongshi_left_a = glLibObjTexCylinder(0.2,0.1,64)
    hongshi_left_b = glLibObjTexDisk(0,0.2,64)
    Objects.append((hongshi_left_a,hongshi_left_b))
    Objects_pos.append([GetCoordX(4),0.15,GetCoordY(1)])
    #hongshi_right
    hongshi_right_a = glLibObjTexCylinder(0.2,0.1,64)
    hongshi_right_b = glLibObjTexDisk(0,0.2,64)
    Objects.append((hongshi_right_a,hongshi_right_b))
    Objects_pos.append([GetCoordX(6),0.15,GetCoordY(1)])
    #hongxiang_left
    hongxiang_left_a = glLibObjTexCylinder(0.2,0.1,64)
    hongxiang_left_b = glLibObjTexDisk(0,0.2,64)
    Objects.append((hongxiang_left_a,hongxiang_left_b))
    Objects_pos.append([GetCoordX(3),0.15,GetCoordY(1)])
    #hongxiang_right
    hongxiang_right_a = glLibObjTexCylinder(0.2,0.1,64)
    hongxiang_right_b = glLibObjTexDisk(0,0.2,64)
    Objects.append((hongxiang_right_a,hongxiang_right_b))
    Objects_pos.append([GetCoordX(7),0.15,GetCoordY(1)])
    #hongbing_1
    hongbing_1_a = glLibObjTexCylinder(0.2,0.1,64)
    hongbing_1_b = glLibObjTexDisk(0,0.2,64)
    Objects.append((hongbing_1_a,hongbing_1_b))
    Objects_pos.append([GetCoordX(1),0.15,GetCoordY(4)])
    #hongbing_2
    hongbing_2_a = glLibObjTexCylinder(0.2,0.1,64)
    hongbing_2_b = glLibObjTexDisk(0,0.2,64)
    Objects.append((hongbing_2_a,hongbing_2_b))
    Objects_pos.append([GetCoordX(3),0.15,GetCoordY(4)])
    #hongbing_3
    hongbing_3_a = glLibObjTexCylinder(0.2,0.1,64)
    hongbing_3_b = glLibObjTexDisk(0,0.2,64)
    Objects.append((hongbing_3_a,hongbing_3_b))
    Objects_pos.append([GetCoordX(5),0.15,GetCoordY(4)])
    #hongbing_4
    hongbing_4_a = glLibObjTexCylinder(0.2,0.1,64)
    hongbing_4_b = glLibObjTexDisk(0,0.2,64)
    Objects.append((hongbing_4_a,hongbing_4_b))
    Objects_pos.append([GetCoordX(7),0.15,GetCoordY(4)])
    #hongbing_5
    hongbing_5_a = glLibObjTexCylinder(0.2,0.1,64)
    hongbing_5_b = glLibObjTexDisk(0,0.2,64)
    Objects.append((hongbing_5_a,hongbing_5_b))
    Objects_pos.append([GetCoordX(9),0.15,GetCoordY(4)])

    #heijiang
    heijiang_a = glLibObjTexCylinder(0.2,0.1,64)
    heijiang_b = glLibObjTexDisk(0,0.2,64)
    Objects.append((heijiang_a,heijiang_b))
    Objects_pos.append([GetCoordX(5),0.15,GetCoordY(10)])
    #heiju_left
    heiju_left_a = glLibObjTexCylinder(0.2,0.1,64)
    heiju_left_b = glLibObjTexDisk(0,0.2,64)
    Objects.append((heiju_left_a,heiju_left_b))
    Objects_pos.append([GetCoordX(1),0.15,GetCoordY(10)])
    #heiju_right
    heiju_right_a = glLibObjTexCylinder(0.2,0.1,64)
    heiju_right_b = glLibObjTexDisk(0,0.2,64)
    Objects.append((heiju_right_a,heiju_right_b))
    Objects_pos.append([GetCoordX(9),0.15,GetCoordY(10)])
    #heima_left
    heima_left_a = glLibObjTexCylinder(0.2,0.1,64)
    heima_left_b = glLibObjTexDisk(0,0.2,64)
    Objects.append((heima_left_a,heima_left_b))
    Objects_pos.append([GetCoordX(2),0.15,GetCoordY(10)])
    #heima_right
    heima_right_a = glLibObjTexCylinder(0.2,0.1,64)
    heima_right_b = glLibObjTexDisk(0,0.2,64)
    Objects.append((heima_right_a,heima_right_b))
    Objects_pos.append([GetCoordX(8),0.15,GetCoordY(10)])
    #heipao_left
    heipao_left_a = glLibObjTexCylinder(0.2,0.1,64)
    heipao_left_b = glLibObjTexDisk(0,0.2,64)
    Objects.append((heipao_left_a,heipao_left_b))
    Objects_pos.append([GetCoordX(2),0.15,GetCoordY(8)])
    #heipao_right
    heipao_right_a = glLibObjTexCylinder(0.2,0.1,64)
    heipao_right_b = glLibObjTexDisk(0,0.2,64)
    Objects.append((heipao_right_a,heipao_right_b))
    Objects_pos.append([GetCoordX(8),0.15,GetCoordY(8)])
    #heishi_left
    heishi_left_a = glLibObjTexCylinder(0.2,0.1,64)
    heishi_left_b = glLibObjTexDisk(0,0.2,64)
    Objects.append((heishi_left_a,heishi_left_b))
    Objects_pos.append([GetCoordX(4),0.15,GetCoordY(10)])
    #heishi_right
    heishi_right_a = glLibObjTexCylinder(0.2,0.1,64)
    heishi_right_b = glLibObjTexDisk(0,0.2,64)
    Objects.append((heishi_right_a,heishi_right_b))
    Objects_pos.append([GetCoordX(6),0.15,GetCoordY(10)])
    #heixiang_left
    heixiang_left_a = glLibObjTexCylinder(0.2,0.1,64)
    heixiang_left_b = glLibObjTexDisk(0,0.2,64)
    Objects.append((heixiang_left_a,heixiang_left_b))
    Objects_pos.append([GetCoordX(3),0.15,GetCoordY(10)])
    #heixiang_right
    heixiang_right_a = glLibObjTexCylinder(0.2,0.1,64)
    heixiang_right_b = glLibObjTexDisk(0,0.2,64)
    Objects.append((heixiang_right_a,heixiang_right_b))
    Objects_pos.append([GetCoordX(7),0.15,GetCoordY(10)])
    #heizu_1
    heizu_1_a = glLibObjTexCylinder(0.2,0.1,64)
    heizu_1_b = glLibObjTexDisk(0,0.2,64)
    Objects.append((heizu_1_a,heizu_1_b))
    Objects_pos.append([GetCoordX(1),0.15,GetCoordY(7)])
    #heizu_2
    heizu_2_a = glLibObjTexCylinder(0.2,0.1,64)
    heizu_2_b = glLibObjTexDisk(0,0.2,64)
    Objects.append((heizu_2_a,heizu_2_b))
    Objects_pos.append([GetCoordX(3),0.15,GetCoordY(7)])
    #heizu_3
    heizu_3_a = glLibObjTexCylinder(0.2,0.1,64)
    heizu_3_b = glLibObjTexDisk(0,0.2,64)
    Objects.append((heizu_3_a,heizu_3_b))
    Objects_pos.append([GetCoordX(5),0.15,GetCoordY(7)])
    #heizu_4
    heizu_4_a = glLibObjTexCylinder(0.2,0.1,64)
    heizu_4_b = glLibObjTexDisk(0,0.2,64)
    Objects.append((heizu_4_a,heizu_4_b))
    Objects_pos.append([GetCoordX(7),0.15,GetCoordY(7)])
    #heizu_5
    heizu_5_a = glLibObjTexCylinder(0.2,0.1,64)
    heizu_5_b = glLibObjTexDisk(0,0.2,64)
    Objects.append((heizu_5_a,heizu_5_b))
    Objects_pos.append([GetCoordX(9),0.15,GetCoordY(7)])

    #cursor
    cursor = glLibObjTexCube((0.4,0.01,0.4))
    Objects.append(cursor)
    Objects_pos.append([GetCoordX(9),0.15,GetCoordY(7)])
    #left_bar
    left_bar = glLibObjTexCube((2.0,0.1,5.0))
    Objects.append(left_bar)
    Objects_pos.append([-3.25,0,0])
    #right_bar
    right_bar = glLibObjTexCube((2.0,0.1,5.0))
    Objects.append(right_bar)
    Objects_pos.append([3.25,0,0])
    #welcome
    welcome = glLibObjTexCube((5.0,0.1,3.0))
    Objects.append(welcome)
    Objects_pos.append([0,10,0])

    #--buttons--
    #instruction
    instruction = glLibObjTexCube((1.6,0.1,0.4))
    Objects.append(instruction)
    Objects_pos.append([-3.2,0.1,-1.0])
    #restart
    restart = glLibObjTexCube((1.6,0.1,0.4))
    Objects.append(restart)
    Objects_pos.append([-3.2,0.1,-0.2])
    #save
    save = glLibObjTexCube((1.6,0.1,0.4))
    Objects.append(save)
    Objects_pos.append([-3.2,0.1,0.6])
    #load
    load = glLibObjTexCube((1.6,0.1,0.4))
    Objects.append(load)
    Objects_pos.append([-3.2,0.1,1.4])
    #regret
    regret = glLibObjTexCube((0.8,0.1,0.8))
    Objects.append(regret)
    Objects_pos.append([3.2,0.1,0.0])

    #chosen
    chosen = glLibObjTexCube((0.4,0.1,0.4))
    Objects.append(chosen)
    Objects_pos.append([0.0,-0.15,0.0])
    #instruction_board
    instruction_board = glLibObjTexCube((6.0,0.01,5.7))
    Objects.append(instruction_board)
    Objects_pos.append([0.0,-10.0,0.0])
    #Redwin
    Redwin = glLibObjText(u"��ʤ����Ϸ����",Font,(255,0,0))
    Objects.append(Redwin)
    Objects_pos.append([-3.5,-20.0,0.5])
    #Blawin
    Blawin = glLibObjText(u"��ʤ����Ϸ����",Font,(0,0,0))
    Objects.append(Blawin)
    Objects_pos.append([-3.5,-20.0,0.5])
    #Saveboard1
    Saveboard1 = glLibObjTexCube((10.0,0.2,1.0))
    Objects.append(Saveboard1)
    Objects_pos.append([2.0,-40.0,-3.85])
    #Saveboard2
    Saveboard2 = glLibObjTexCube((10.0,0.2,1.0))
    Objects.append(Saveboard2)
    Objects_pos.append([2.0,-40.0,-2.75])
    #Saveboard3
    Saveboard3 = glLibObjTexCube((10.0,0.2,1.0))
    Objects.append(Saveboard3)
    Objects_pos.append([2.0,-40.0,-1.65])
    #Saveboard4
    Saveboard4 = glLibObjTexCube((10.0,0.2,1.0))
    Objects.append(Saveboard4)
    Objects_pos.append([2.0,-40.0,-0.55])
    #Saveboard5
    Saveboard5 = glLibObjTexCube((10.0,0.2,1.0))
    Objects.append(Saveboard5)
    Objects_pos.append([2.0,-40.0,0.55])
    #Saveboard6
    Saveboard6 = glLibObjTexCube((10.0,0.2,1.0))
    Objects.append(Saveboard6)
    Objects_pos.append([2.0,-40.0,1.65])
    #Saveboard7
    Saveboard7 = glLibObjTexCube((10.0,0.2,1.0))
    Objects.append(Saveboard7)
    Objects_pos.append([2.0,-40.0,2.75])
    #Saveboard8
    Saveboard8 = glLibObjTexCube((10.0,0.2,1.0))
    Objects.append(Saveboard8)
    Objects_pos.append([2.0,-40.0,3.85])
    #Save1
    Save1 = glLibObjText(Chess_ls[0],Font,(0,0,0))
    Objects.append(Save1)
    Objects_pos.append([-3.0,-39.88,-3.35])
    #Save2
    Save2 = glLibObjText(Chess_ls[1],Font,(0,0,0))
    Objects.append(Save2)
    Objects_pos.append([-3.0,-39.88,-2.25])
    #Save3
    Save3 = glLibObjText(Chess_ls[2],Font,(0,0,0))
    Objects.append(Save3)
    Objects_pos.append([-3.0,-39.88,-1.15])
    #Save4
    Save4 = glLibObjText(Chess_ls[3],Font,(0,0,0))
    Objects.append(Save4)
    Objects_pos.append([-3.0,-39.88,-0.05])
    #Save5
    Save5 = glLibObjText(Chess_ls[4],Font,(0,0,0))
    Objects.append(Save5)
    Objects_pos.append([-3.0,-39.88,0.95])
    #Save6
    Save6 = glLibObjText(Chess_ls[5],Font,(0,0,0))
    Objects.append(Save6)
    Objects_pos.append([-3.0,-39.88,2.05])
    #Save7
    Save7 = glLibObjText(Chess_ls[6],Font,(0,0,0))
    Objects.append(Save7)
    Objects_pos.append([-3.0,-39.88,3.15])
    #Save8
    Save8 = glLibObjText(Chess_ls[7],Font,(0,0,0))
    Objects.append(Save8)
    Objects_pos.append([-3.0,-39.88,4.25])
    #Return_Button
    Return_Button = glLibObjTexCube((2.0,0.2,2.0))
    Objects.append(Return_Button)
    Objects_pos.append([-4.5,-40.0,3.25])
    #Return_moji
    Return_moji = glLibObjText(u"����",Font,(0,0,0))
    Objects.append(Return_moji)
    Objects_pos.append([-5.5,-39.88,3.75])


def GetInput():
    global flag
    mpress = pygame.mouse.get_pressed()
    mrel = pygame.mouse.get_rel()
    key = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            cursor_pos = glLibUnProject(pygame.mouse.get_pos())
            return cursor_pos[0],cursor_pos[2],False,True,False

        if event.type == MOUSEBUTTONUP:
            if mpress[0]:
                cursor_pos = glLibUnProject(pygame.mouse.get_pos())
                return cursor_pos[0],cursor_pos[2],True,False,True
            else:
                cursor_pos = glLibUnProject(pygame.mouse.get_pos())
                return cursor_pos[0],cursor_pos[2],False,False,True

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
    if flag:
        if   key[K_LEFT]:
            Camera.set_target_pos([-5.0,0.5,0.0])
        elif key[K_RIGHT]:
            Camera.set_target_pos([6.0,0.5,0.0])
        elif key[K_UP]:
            Camera.set_target_pos([0.0,6.0,0.0000000000001]) #Bug exists if z=0.0
        elif key[K_DOWN]:
            Camera.set_target_pos([0.0,5.0,6.0])
    cursor_pos = glLibUnProject(pygame.mouse.get_pos())
    return cursor_pos[0],cursor_pos[2],False,False,False

def Update():
    Camera.update()


def DrawChessboard():
    glBindTexture(GL_TEXTURE_2D, Texture[0])
    Objects[0].draw(Objects_pos[0])
    #hongshuai
    glBindTexture(GL_TEXTURE_2D, Texture[15])
    Objects[1][0].draw(Objects_pos[1],[[90,0,0]])
    glBindTexture(GL_TEXTURE_2D, Texture[1])
    Objects[1][1].draw(Objects_pos[1],[[90,180,180]])
    #hongju-left
    glBindTexture(GL_TEXTURE_2D, Texture[15])
    Objects[2][0].draw(Objects_pos[2],[[90,0,0]])
    glBindTexture(GL_TEXTURE_2D, Texture[2])
    Objects[2][1].draw(Objects_pos[2],[[90,180,180]])
    #hongju-right
    glBindTexture(GL_TEXTURE_2D, Texture[15])
    Objects[3][0].draw(Objects_pos[3],[[90,0,0]])
    glBindTexture(GL_TEXTURE_2D, Texture[2])
    Objects[3][1].draw(Objects_pos[3],[[90,180,180]])
    #hongma-left
    glBindTexture(GL_TEXTURE_2D, Texture[15])
    Objects[4][0].draw(Objects_pos[4],[[90,0,0]])
    glBindTexture(GL_TEXTURE_2D, Texture[3])
    Objects[4][1].draw(Objects_pos[4],[[90,180,180]])
    #hongma-right
    glBindTexture(GL_TEXTURE_2D, Texture[15])
    Objects[5][0].draw(Objects_pos[5],[[90,0,0]])
    glBindTexture(GL_TEXTURE_2D, Texture[3])
    Objects[5][1].draw(Objects_pos[5],[[90,180,180]])
    #hongpao-left
    glBindTexture(GL_TEXTURE_2D, Texture[15])
    Objects[6][0].draw(Objects_pos[6],[[90,0,0]])
    glBindTexture(GL_TEXTURE_2D, Texture[4])
    Objects[6][1].draw(Objects_pos[6],[[90,180,180]])
    #hongpao-right
    glBindTexture(GL_TEXTURE_2D, Texture[15])
    Objects[7][0].draw(Objects_pos[7],[[90,0,0]])
    glBindTexture(GL_TEXTURE_2D, Texture[4])
    Objects[7][1].draw(Objects_pos[7],[[90,180,180]])
    #hongshi-left
    glBindTexture(GL_TEXTURE_2D, Texture[15])
    Objects[8][0].draw(Objects_pos[8],[[90,0,0]])
    glBindTexture(GL_TEXTURE_2D, Texture[5])
    Objects[8][1].draw(Objects_pos[8],[[90,180,180]])
    #hongshi-right
    glBindTexture(GL_TEXTURE_2D, Texture[15])
    Objects[9][0].draw(Objects_pos[9],[[90,0,0]])
    glBindTexture(GL_TEXTURE_2D, Texture[5])
    Objects[9][1].draw(Objects_pos[9],[[90,180,180]])
    #hongxiang-left
    glBindTexture(GL_TEXTURE_2D, Texture[15])
    Objects[10][0].draw(Objects_pos[10],[[90,0,0]])
    glBindTexture(GL_TEXTURE_2D, Texture[6])
    Objects[10][1].draw(Objects_pos[10],[[90,180,180]])
    #hongxiang-right
    glBindTexture(GL_TEXTURE_2D, Texture[15])
    Objects[11][0].draw(Objects_pos[11],[[90,0,0]])
    glBindTexture(GL_TEXTURE_2D, Texture[6])
    Objects[11][1].draw(Objects_pos[11],[[90,180,180]])
    #hongbing_1
    glBindTexture(GL_TEXTURE_2D, Texture[15])
    Objects[12][0].draw(Objects_pos[12],[[90,0,0]])
    glBindTexture(GL_TEXTURE_2D, Texture[7])
    Objects[12][1].draw(Objects_pos[12],[[90,180,180]])
    #hongbing_2
    glBindTexture(GL_TEXTURE_2D, Texture[15])
    Objects[13][0].draw(Objects_pos[13],[[90,0,0]])
    glBindTexture(GL_TEXTURE_2D, Texture[7])
    Objects[13][1].draw(Objects_pos[13],[[90,180,180]])
    #hongbing_3
    glBindTexture(GL_TEXTURE_2D, Texture[15])
    Objects[14][0].draw(Objects_pos[14],[[90,0,0]])
    glBindTexture(GL_TEXTURE_2D, Texture[7])
    Objects[14][1].draw(Objects_pos[14],[[90,180,180]])
    #hongbing_4
    glBindTexture(GL_TEXTURE_2D, Texture[15])
    Objects[15][0].draw(Objects_pos[15],[[90,0,0]])
    glBindTexture(GL_TEXTURE_2D, Texture[7])
    Objects[15][1].draw(Objects_pos[15],[[90,180,180]])
    #hongbing_5
    glBindTexture(GL_TEXTURE_2D, Texture[15])
    Objects[16][0].draw(Objects_pos[16],[[90,0,0]])
    glBindTexture(GL_TEXTURE_2D, Texture[7])
    Objects[16][1].draw(Objects_pos[16],[[90,180,180]])

    #heijiang
    glBindTexture(GL_TEXTURE_2D, Texture[15])
    Objects[17][0].draw(Objects_pos[17],[[90,0,0]])
    glBindTexture(GL_TEXTURE_2D, Texture[8])
    Objects[17][1].draw(Objects_pos[17],[[90,180,0]])
    #heiju-left
    glBindTexture(GL_TEXTURE_2D, Texture[15])
    Objects[18][0].draw(Objects_pos[18],[[90,0,0]])
    glBindTexture(GL_TEXTURE_2D, Texture[9])
    Objects[18][1].draw(Objects_pos[18],[[90,180,0]])
    #heiju-right
    glBindTexture(GL_TEXTURE_2D, Texture[15])
    Objects[19][0].draw(Objects_pos[19],[[90,0,0]])
    glBindTexture(GL_TEXTURE_2D, Texture[9])
    Objects[19][1].draw(Objects_pos[19],[[90,180,0]])
    #heima-left
    glBindTexture(GL_TEXTURE_2D, Texture[15])
    Objects[20][0].draw(Objects_pos[20],[[90,0,0]])
    glBindTexture(GL_TEXTURE_2D, Texture[10])
    Objects[20][1].draw(Objects_pos[20],[[90,180,0]])
    #heima-right
    glBindTexture(GL_TEXTURE_2D, Texture[15])
    Objects[21][0].draw(Objects_pos[21],[[90,0,0]])
    glBindTexture(GL_TEXTURE_2D, Texture[10])
    Objects[21][1].draw(Objects_pos[21],[[90,180,0]])
    #heipao-left
    glBindTexture(GL_TEXTURE_2D, Texture[15])
    Objects[22][0].draw(Objects_pos[22],[[90,0,0]])
    glBindTexture(GL_TEXTURE_2D, Texture[11])
    Objects[22][1].draw(Objects_pos[22],[[90,180,0]])
    #heipao-right
    glBindTexture(GL_TEXTURE_2D, Texture[15])
    Objects[23][0].draw(Objects_pos[23],[[90,0,0]])
    glBindTexture(GL_TEXTURE_2D, Texture[11])
    Objects[23][1].draw(Objects_pos[23],[[90,180,0]])
    #heishi-left
    glBindTexture(GL_TEXTURE_2D, Texture[15])
    Objects[24][0].draw(Objects_pos[24],[[90,0,0]])
    glBindTexture(GL_TEXTURE_2D, Texture[12])
    Objects[24][1].draw(Objects_pos[24],[[90,180,0]])
    #heishi-right
    glBindTexture(GL_TEXTURE_2D, Texture[15])
    Objects[25][0].draw(Objects_pos[25],[[90,0,0]])
    glBindTexture(GL_TEXTURE_2D, Texture[12])
    Objects[25][1].draw(Objects_pos[25],[[90,180,0]])
    #heixiang-left
    glBindTexture(GL_TEXTURE_2D, Texture[15])
    Objects[26][0].draw(Objects_pos[26],[[90,0,0]])
    glBindTexture(GL_TEXTURE_2D, Texture[13])
    Objects[26][1].draw(Objects_pos[26],[[90,180,0]])
    #heixiang-right
    glBindTexture(GL_TEXTURE_2D, Texture[15])
    Objects[27][0].draw(Objects_pos[27],[[90,0,0]])
    glBindTexture(GL_TEXTURE_2D, Texture[13])
    Objects[27][1].draw(Objects_pos[27],[[90,180,0]])
    #heibing_1
    glBindTexture(GL_TEXTURE_2D, Texture[15])
    Objects[28][0].draw(Objects_pos[28],[[90,0,0]])
    glBindTexture(GL_TEXTURE_2D, Texture[14])
    Objects[28][1].draw(Objects_pos[28],[[90,180,0]])
    #heibing_2
    glBindTexture(GL_TEXTURE_2D, Texture[15])
    Objects[29][0].draw(Objects_pos[29],[[90,0,0]])
    glBindTexture(GL_TEXTURE_2D, Texture[14])
    Objects[29][1].draw(Objects_pos[29],[[90,180,0]])
    #heibing_3
    glBindTexture(GL_TEXTURE_2D, Texture[15])
    Objects[30][0].draw(Objects_pos[30],[[90,0,0]])
    glBindTexture(GL_TEXTURE_2D, Texture[14])
    Objects[30][1].draw(Objects_pos[30],[[90,180,0]])
    #heibing_4
    glBindTexture(GL_TEXTURE_2D, Texture[15])
    Objects[31][0].draw(Objects_pos[31],[[90,0,0]])
    glBindTexture(GL_TEXTURE_2D, Texture[14])
    Objects[31][1].draw(Objects_pos[31],[[90,180,0]])
    #heibing_5
    glBindTexture(GL_TEXTURE_2D, Texture[15])
    Objects[32][0].draw(Objects_pos[32],[[90,0,0]])
    glBindTexture(GL_TEXTURE_2D, Texture[14])
    Objects[32][1].draw(Objects_pos[32],[[90,180,0]])
    #cursor
    glBindTexture(GL_TEXTURE_2D, Texture[16])
    Objects[33].draw(Objects_pos[33])
    #left_bar
    glBindTexture(GL_TEXTURE_2D, Texture[17])
    Objects[34].draw(Objects_pos[34])
    #right_bar
    glBindTexture(GL_TEXTURE_2D, Texture[18])
    Objects[35].draw(Objects_pos[35])
    #welcome_bar
    glBindTexture(GL_TEXTURE_2D, Texture[19])
    Objects[36].draw(Objects_pos[36])

    #instruction
    glBindTexture(GL_TEXTURE_2D, Texture[20])
    Objects[37].draw(Objects_pos[37])
    #restart
    glBindTexture(GL_TEXTURE_2D, Texture[21])
    Objects[38].draw(Objects_pos[38])
    #save
    glBindTexture(GL_TEXTURE_2D, Texture[22])
    Objects[39].draw(Objects_pos[39])
    #load
    glBindTexture(GL_TEXTURE_2D, Texture[23])
    Objects[40].draw(Objects_pos[40])
    #regret
    glBindTexture(GL_TEXTURE_2D, Texture[24])
    Objects[41].draw(Objects_pos[41])
    #chosen
    glBindTexture(GL_TEXTURE_2D, Texture[25])
    Objects[42].draw(Objects_pos[42])
    #instruction_board
    glBindTexture(GL_TEXTURE_2D, Texture[26])
    Objects[43].draw(Objects_pos[43])
    #Redwin
    Objects[44].draw(Objects_pos[44],[[270,0,0]])
    #Blawin
    Objects[45].draw(Objects_pos[45],[[270,0,0]])
    #Saveboard1
    glBindTexture(GL_TEXTURE_2D, Texture[27])
    Objects[46].draw(Objects_pos[46])
    #Saveboard2
    glBindTexture(GL_TEXTURE_2D, Texture[27])
    Objects[47].draw(Objects_pos[47])
    #Saveboard3
    glBindTexture(GL_TEXTURE_2D, Texture[27])
    Objects[48].draw(Objects_pos[48])
    #Saveboard4
    glBindTexture(GL_TEXTURE_2D, Texture[27])
    Objects[49].draw(Objects_pos[49])
    #Saveboard5
    glBindTexture(GL_TEXTURE_2D, Texture[27])
    Objects[50].draw(Objects_pos[50])
    #Saveboard6
    glBindTexture(GL_TEXTURE_2D, Texture[27])
    Objects[51].draw(Objects_pos[51])
    #Saveboard7
    glBindTexture(GL_TEXTURE_2D, Texture[27])
    Objects[52].draw(Objects_pos[52])
    #Saveboard8
    glBindTexture(GL_TEXTURE_2D, Texture[27])
    Objects[53].draw(Objects_pos[53])
    #Save1
    Objects[54].draw(Objects_pos[54],[[270,0,0]])
    #Save2
    Objects[55].draw(Objects_pos[55],[[270,0,0]])
    #Save3
    Objects[56].draw(Objects_pos[56],[[270,0,0]])
    #Save4
    Objects[57].draw(Objects_pos[57],[[270,0,0]])
    #Save5
    Objects[58].draw(Objects_pos[58],[[270,0,0]])
    #Save6
    Objects[59].draw(Objects_pos[59],[[270,0,0]])
    #Save7
    Objects[60].draw(Objects_pos[60],[[270,0,0]])
    #Save8
    Objects[61].draw(Objects_pos[61],[[270,0,0]])

    #Return_Button
    glBindTexture(GL_TEXTURE_2D, Texture[27])
    Objects[62].draw(Objects_pos[62])
    #Return_moji
    Objects[63].draw(Objects_pos[63],[[270,0,0]])


def Draw():
    Window.clear()
    Camera.set_camera()
    Sun1.enable()
    Sun2.enable()
    Sun3.enable()
    Sun4.enable()
    Sun1.draw()
    Sun2.draw()
    Sun3.draw()
    Sun4.draw()
    DrawChessboard()

    Window.flip()


def Instruction():
    Camera.set_target_pos([0,-3.0,0.00000001]) #Bug exists if z=0.0
    Camera.set_target_center([0,-15.0,0.00000001]) #Bug exists if z=0.0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if (event.type == MOUSEBUTTONUP) or (event.type == KEYDOWN):
                Camera.set_target_pos([0.0,6.0,0.00000001]) #Bug exists if z=0.0
                Camera.set_target_center([0,0,0.0])
                pygame.event.clear()
                return
        Update()
        Draw()


def Restart():
    Init()
    DeleteAll()
    drawBoard()
    drawChess()
    return


def Save():
    global flag
    flag = False
    Camera.set_target_pos([0,-25.0,0.00000001]) #Bug exists if z=0.0
    Camera.set_target_center([0,-35.0,0.00000001]) #Bug exists if z=0.0
    mpress = pygame.mouse.get_pressed()
    while True:
        raw_x, raw_y, is_pressed, is_down, is_up = GetInput()
        if is_up:
            for i in range(46,54):
                Objects_pos[i][1] = -40.0
            for i in range(54,62):
                Objects_pos[i][1] = -39.88
        if (raw_x >= -3.0 and raw_x <= 3.0):
            if (raw_y >= -4.35 and raw_y <= -3.35):
                if is_pressed:
                    filename = SaveOrLoad(("save",0))
                    Objects[54] = glLibObjText(filename,Font,(0,0,0))
                if is_down:
                    Objects_pos[46][1] -= 0.1
                    Objects_pos[54][1] -= 0.1
            if (raw_y >= -3.25 and raw_y <= -2.25):
                if is_pressed:
                    filename = SaveOrLoad(("save",1))
                    Objects[55] = glLibObjText(filename,Font,(0,0,0))
                if is_down:
                    Objects_pos[47][1] -= 0.1
                    Objects_pos[55][1] -= 0.1
            if (raw_y >= -2.15 and raw_y <= -1.15):
                if is_pressed:
                    filename = SaveOrLoad(("save",2))
                    Objects[56] = glLibObjText(filename,Font,(0,0,0))
                if is_down:
                    Objects_pos[48][1] -= 0.1
                    Objects_pos[56][1] -= 0.1
            if (raw_y >= -1.05 and raw_y <= -0.05):
                if is_pressed:
                    filename = SaveOrLoad(("save",3))
                    Objects[57] = glLibObjText(filename,Font,(0,0,0))
                if is_down:
                    Objects_pos[49][1] -= 0.1
                    Objects_pos[57][1] -= 0.1
            if (raw_y >= 0.05 and raw_y <= 1.05):
                if is_pressed:
                    filename = SaveOrLoad(("save",4))
                    Objects[58] = glLibObjText(filename,Font,(0,0,0))
                if is_down:
                    Objects_pos[50][1] -= 0.1
                    Objects_pos[58][1] -= 0.1
            if (raw_y >= 1.15 and raw_y <= 2.25):
                if is_pressed:
                    filename = SaveOrLoad(("save",5))
                    Objects[59] = glLibObjText(filename,Font,(0,0,0))
                if is_down:
                    Objects_pos[51][1] -= 0.1
                    Objects_pos[59][1] -= 0.1
            if (raw_y >= 2.25 and raw_y <= 3.35):
                if is_pressed:
                    filename = SaveOrLoad(("save",6))
                    Objects[60] = glLibObjText(filename,Font,(0,0,0))
                if is_down:
                    Objects_pos[52][1] -= 0.1
                    Objects_pos[60][1] -= 0.1
            if (raw_y >= 3.35 and raw_y <= 4.45):
                if is_pressed:
                    filename = SaveOrLoad(("save",7))
                    Objects[61] = glLibObjText(filename,Font,(0,0,0))
                if is_down:
                    Objects_pos[53][1] -= 0.1
                    Objects_pos[61][1] -= 0.1
        if (raw_x >= -5.5 and raw_x <= -3.5 and raw_y >= 2.25 and raw_y <= 4.25):
            if is_pressed:
                Camera.set_target_pos([0.0,6.0,0.00000001]) #Bug exists if z=0.0
                Camera.set_target_center([0,0,0])
                pygame.event.clear()
                return

        Update()
        Draw()


def Load():
    global flag
    flag = False
    Camera.set_target_pos([0,-25.0,0.00000001]) #Bug exists if z=0.0
    Camera.set_target_center([0,-35.0,0.00000001]) #Bug exists if z=0.0
    mpress = pygame.mouse.get_pressed()
    while True:
        raw_x, raw_y, is_pressed, is_down, is_up = GetInput()
        if is_up:
            for i in range(46,54):
                Objects_pos[i][1] = -40.0
            for i in range(54,62):
                Objects_pos[i][1] = -39.88
        if (raw_x >= -3.0 and raw_x <= 3.0):
            if (raw_y >= -4.35 and raw_y <= -3.35):
                if is_pressed:
                    ls = SaveOrLoad(("load",0))
                    for i in range(1,33):
                        Objects_pos[i][1] = -0.15
                    for order in ls:
                        if order[1] == 2:
                            Objects_pos[order[0]][0] = GetCoordX(order[2])
                            Objects_pos[order[0]][2] = GetCoordY(order[3])
                            Objects_pos[order[0]][1] = 0.15
                        else:
                            print 'error'
                    Camera.set_target_pos([0.0,6.0,0.00000001]) #Bug exists if z=0.0
                    Camera.set_target_center([0,0,0])
                    pygame.event.clear()
                    return
                if is_down:
                    Objects_pos[46][1] -= 0.1
                    Objects_pos[54][1] -= 0.1
            if (raw_y >= -3.25 and raw_y <= -2.25):
                if is_pressed:
                    ls = SaveOrLoad(("load",1))
                    for i in range(1,33):
                        Objects_pos[i][1] = -0.15
                    for order in ls:
                        if order[1] == 2:
                            Objects_pos[order[0]][0] = GetCoordX(order[2])
                            Objects_pos[order[0]][2] = GetCoordY(order[3])
                            Objects_pos[order[0]][1] = 0.15
                        else:
                            print 'error'
                    Camera.set_target_pos([0.0,6.0,0.00000001]) #Bug exists if z=0.0
                    Camera.set_target_center([0,0,0])
                    pygame.event.clear()
                    return
                if is_down:
                    Objects_pos[47][1] -= 0.1
                    Objects_pos[55][1] -= 0.1
            if (raw_y >= -2.15 and raw_y <= -1.15):
                if is_pressed:
                    ls = SaveOrLoad(("load",2))
                    for i in range(1,33):
                        Objects_pos[i][1] = -0.15
                    for order in ls:
                        if order[1] == 2:
                            Objects_pos[order[0]][0] = GetCoordX(order[2])
                            Objects_pos[order[0]][2] = GetCoordY(order[3])
                            Objects_pos[order[0]][1] = 0.15
                        else:
                            print 'error'
                    Camera.set_target_pos([0.0,6.0,0.00000001]) #Bug exists if z=0.0
                    Camera.set_target_center([0,0,0])
                    pygame.event.clear()
                    return
                if is_down:
                    Objects_pos[48][1] -= 0.1
                    Objects_pos[56][1] -= 0.1
            if (raw_y >= -1.05 and raw_y <= -0.05):
                if is_pressed:
                    ls = SaveOrLoad(("load",3))
                    for i in range(1,33):
                        Objects_pos[i][1] = -0.15
                    for order in ls:
                        if order[1] == 2:
                            Objects_pos[order[0]][0] = GetCoordX(order[2])
                            Objects_pos[order[0]][2] = GetCoordY(order[3])
                            Objects_pos[order[0]][1] = 0.15
                        else:
                            print 'error'
                    Camera.set_target_pos([0.0,6.0,0.00000001]) #Bug exists if z=0.0
                    Camera.set_target_center([0,0,0])
                    pygame.event.clear()
                    return
                if is_down:
                    Objects_pos[49][1] -= 0.1
                    Objects_pos[57][1] -= 0.1
            if (raw_y >= 0.05 and raw_y <= 1.05):
                if is_pressed:
                    ls = SaveOrLoad(("load",4))
                    for i in range(1,33):
                        Objects_pos[i][1] = -0.15
                    for order in ls:
                        if order[1] == 2:
                            Objects_pos[order[0]][0] = GetCoordX(order[2])
                            Objects_pos[order[0]][2] = GetCoordY(order[3])
                            Objects_pos[order[0]][1] = 0.15
                        else:
                            print 'error'
                    Camera.set_target_pos([0.0,6.0,0.00000001]) #Bug exists if z=0.0
                    Camera.set_target_center([0,0,0])
                    pygame.event.clear()
                    return
                if is_down:
                    Objects_pos[50][1] -= 0.1
                    Objects_pos[58][1] -= 0.1
            if (raw_y >= 1.15 and raw_y <= 2.25):
                if is_pressed:
                    ls = SaveOrLoad(("load",5))
                    for i in range(1,33):
                        Objects_pos[i][1] = -0.15
                    for order in ls:
                        if order[1] == 2:
                            Objects_pos[order[0]][0] = GetCoordX(order[2])
                            Objects_pos[order[0]][2] = GetCoordY(order[3])
                            Objects_pos[order[0]][1] = 0.15
                        else:
                            print 'error'
                    Camera.set_target_pos([0.0,6.0,0.00000001]) #Bug exists if z=0.0
                    Camera.set_target_center([0,0,0])
                    pygame.event.clear()
                    return
                if is_down:
                    Objects_pos[51][1] -= 0.1
                    Objects_pos[59][1] -= 0.1
            if (raw_y >= 2.25 and raw_y <= 3.35):
                if is_pressed:
                    ls = SaveOrLoad(("load",6))
                    for i in range(1,33):
                        Objects_pos[i][1] = -0.15
                    for order in ls:
                        if order[1] == 2:
                            Objects_pos[order[0]][0] = GetCoordX(order[2])
                            Objects_pos[order[0]][2] = GetCoordY(order[3])
                            Objects_pos[order[0]][1] = 0.15
                        else:
                            print 'error'
                    Camera.set_target_pos([0.0,6.0,0.00000001]) #Bug exists if z=0.0
                    Camera.set_target_center([0,0,0])
                    pygame.event.clear()
                    return
                if is_down:
                    Objects_pos[52][1] -= 0.1
                    Objects_pos[60][1] -= 0.1
            if (raw_y >= 3.35 and raw_y <= 4.45):
                if is_pressed:
                    ls = SaveOrLoad(("load",7))
                    for i in range(1,33):
                        Objects_pos[i][1] = -0.15
                    for order in ls:
                        if order[1] == 2:
                            Objects_pos[order[0]][0] = GetCoordX(order[2])
                            Objects_pos[order[0]][2] = GetCoordY(order[3])
                            Objects_pos[order[0]][1] = 0.15
                        else:
                            print 'error'
                    Camera.set_target_pos([0.0,6.0,0.00000001]) #Bug exists if z=0.0
                    Camera.set_target_center([0,0,0])
                    pygame.event.clear()
                    return
                if is_down:
                    Objects_pos[53][1] -= 0.1
                    Objects_pos[61][1] -= 0.1
        if (raw_x >= -5.5 and raw_x <= -3.5 and raw_y >= 2.25 and raw_y <= 4.25):
            if is_pressed:
                Camera.set_target_pos([0.0,6.0,0.00000001]) #Bug exists if z=0.0
                Camera.set_target_center([0,0,0])
                pygame.event.clear()
                return

        Update()
        Draw()


def Regret():
    WalkMethod = toPreState()
    for order in WalkMethod:
        if order[1] == -1:
            Objects_pos[order[0]][1] = -0.15
        elif order[1] == 0:
            Objects_pos[order[0]][1] = 0.15
            Objects_pos[42] = [0.0,-0.15,0.0]
        elif order[1] == 1:
            Objects_pos[order[0]][1] = 0.35
            Objects_pos[42] = [Objects_pos[order[0]][0],0.3,Objects_pos[order[0]][2]]
        elif order[1] == 2:
            Objects_pos[order[0]][0] = GetCoordX(order[2])
            Objects_pos[order[0]][2] = GetCoordY(order[3])
            Objects_pos[order[0]][1] = 0.15
    return


def Main_Title():
    global flag
    flag = False
    Camera.set_target_pos([0,13.5,0.00000001]) #Bug exists if z=0.0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if (event.type == MOUSEBUTTONUP) or (event.type == KEYDOWN):
                Camera.set_target_pos([0.0,6.0,0.00000001]) #Bug exists if z=0.0
                pygame.event.clear()
                return
        Update()
        Draw()


def Main_Loop():
    global Objects_pos,flag
    while True:
        flag = True
        raw_x, raw_y, is_pressed, is_down, is_up = GetInput()
        mouse_x, mouse_y = int(round(GetMessX(raw_x))),int(round(GetMessY(raw_y)))
        if is_up:
            Objects_pos[37][1] = Objects_pos[38][1] = Objects_pos[39][1] = Objects_pos[40][1] = Objects_pos[41][1] = 0.1
        if (raw_x>=-4.0 and raw_x<=-2.4):
            if (raw_y>-1.2 and raw_y<=-0.8):
                if is_down:
                    Objects_pos[37][1] -= 0.06
                    print "instruction"
                if is_pressed:
                    Instruction()
            elif (raw_y>-0.4 and raw_y<=0.0):
                if is_down:
                    Objects_pos[38][1] -= 0.06
                    print "restart"
                if is_pressed:
                    Restart()
            elif (raw_y>0.4 and raw_y<=0.8):
                if is_down:
                    Objects_pos[39][1] -= 0.06
                    print "save"
                if is_pressed:
                    Save()
            elif (raw_y>1.2 and raw_y<=1.6):
                if is_down:
                    Objects_pos[40][1] -= 0.06
                    print "load"
                if is_pressed:
                    Load()
        elif (raw_x>=2.8 and raw_x<=3.6 and raw_y>=-0.4 and raw_y<=0.4):
            if is_down:
                Objects_pos[41][1] -= 0.06
                print "regret"
            if is_pressed:
                Regret()
        elif (mouse_x >=1 and mouse_x <=9 and mouse_y>=1 and mouse_y<=10):
            if is_pressed:
                #Showit()
                #print 'A',mouse_x,mouse_y
                WalkMethod = getEachXY(mouse_x, mouse_y)
                for order in WalkMethod:
                    if order[1] == -1:
                        Objects_pos[order[0]][1] = -0.15
                    elif order[1] == 0:
                        Objects_pos[order[0]][1] = 0.15
                        Objects_pos[42] = [0.0,-0.15,0.0]
                    elif order[1] == 1:
                        Objects_pos[order[0]][1] = 0.35
                        Objects_pos[42] = [Objects_pos[order[0]][0],0.3,Objects_pos[order[0]][2]]
                    elif order[1] == 2:
                        Objects_pos[order[0]][0] = GetCoordX(order[2])
                        Objects_pos[order[0]][2] = GetCoordY(order[3])
                        Objects_pos[42] = [0.0,-0.15,0.0]
                        winner = getwinner()
                        if winner == 0:
                            Objects_pos[44][1] = 0.5
                        elif winner == 2:
                            Objects_pos[45][1] = 0.5
            Objects_pos[33] = [GetCoordX(mouse_x),0.15,GetCoordY(mouse_y)]
        #elif mouse_x==12 and is_pressed:
        #    Main_Title()
        Update()
        Draw()

def main():
    Init()
    drawBoard()
    drawChess()
    Main_Title()
    Main_Loop()

if __name__ == '__main__': main()
