import pygame
from pygame.locals import *

pygame.init()
font = pygame.font.SysFont(None, 24)

running = True
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("SAT Adventure")

velocity = 30
questionNumber = 0
questionNumberm = 0
questionNumberforCheckEla = -1
questionNumberforCheckMath = -1
score = 0
surface = "start screen"

textColor1 = (255, 255, 255)
textColor2 = (0, 0, 0)

base_path = "/Users/saisirasapalli/IdeaProjects/IB Computer Science SL Projects/Congressional App Challenge/"

with open(base_path + "MathQuestions.txt", "r") as m:
    Mathquestions = m.readlines()

with open(base_path + "ElaQuestions.txt", "r") as e:
    ELAquestions = e.readlines()

with open(base_path + "MathCorrect.txt", "r") as a:
    MathAnswers = a.readlines()

with open(base_path + "ElaCorrect.txt", "r") as b:
    ElaAnswers = b.readlines()


def checkCorrectAnswer(
    questionType, userAnswer, questionNumberforCheckEla, questionNumberforCheckMath
):
    global score
    if questionType == "Ela":
        correctAnswer = ElaAnswers[questionNumberforCheckEla].strip()
    elif questionType == "Math":
        correctAnswer = MathAnswers[questionNumberforCheckMath].strip()
    else:
        return False

    if str(userAnswer).strip() == correctAnswer:
        score += 1
        return True
    return False


def displayQuestion(questionNumber):
    currentQuestion = ""
    for x in range(15):
        currentQuestion = currentQuestion + ELAquestions[x + questionNumber]
    return currentQuestion


def displayQuestionm(questionNumberm):
    currentQuestionm = ""
    for x in range(8):
        currentQuestionm = currentQuestionm + Mathquestions[x + questionNumberm]
    return currentQuestionm


class Werewolf(pygame.sprite.Sprite):

    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(base_path + "Werewolf.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (110, 110))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        

class ElaGhost(pygame.sprite.Sprite):

    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(base_path + "ElaGhost.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


class MathGhost(pygame.sprite.Sprite):

    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(base_path + "MathGhost.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


class Door(pygame.sprite.Sprite):

    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(base_path + "ExitDoor.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


class Background(pygame.sprite.Sprite):

    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            base_path + "GameBackground.png"
        ).convert_alpha()
        self.image = pygame.transform.scale(self.image, (800, 800))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


Werewolf1 = Werewolf([320, 335])

ElaGhost1 = ElaGhost([685, 385])
ElaGhost2 = ElaGhost([655, 515])
ElaGhost3 = ElaGhost([572, 620])
ElaGhost4 = ElaGhost([452, 677])
ElaGhost5 = ElaGhost([318, 677])
ElaGhost6 = ElaGhost([198, 620])
ElaGhost7 = ElaGhost([115, 515])

MathGhost1 = MathGhost([85, 385])
MathGhost2 = MathGhost([115, 255])
MathGhost3 = MathGhost([198, 150])
MathGhost4 = MathGhost([318, 93])
MathGhost5 = MathGhost([452, 93])
MathGhost6 = MathGhost([572, 150])
MathGhost7 = MathGhost([655, 255])

ExitDoor = Door([372, 360])
GameBackground = Background([0, 0])

ElaGhost1Exist = True
ElaGhost2Exist = True
ElaGhost3Exist = True
ElaGhost4Exist = True
ElaGhost5Exist = True
ElaGhost6Exist = True
ElaGhost7Exist = True

MathGhost1Exist = True
MathGhost2Exist = True
MathGhost3Exist = True
MathGhost4Exist = True
MathGhost5Exist = True
MathGhost6Exist = True
MathGhost7Exist = True

if surface == "start screen":
        screen.fill((255, 255, 255))
        with open(
            "/Users/saisirasapalli/IdeaProjects/IB Computer Science SL Projects/Congressional App Challenge/score.txt",
            "r",
        ) as f:
            try:
                tryscore = int(f.read())
            except ValueError:
                tryscore = 0
        startScreenText = font.render(
            f"Your previous score was: {tryscore}, can you beat that? \n Press SPACE to Start",
            True,
            (0, 0, 0),
        )
 


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_a] and surface == "game":
                        if Werewolf1.rect.left - velocity > 0:
                            Werewolf1.rect.left -= velocity
                        else:
                            Werewolf1.rect.left = 0
                    if keys[pygame.K_d] and surface == "game":
                        if Werewolf1.rect.left + velocity < screen.get_width():
                            Werewolf1.rect.left += velocity
                        else:
                            Werewolf1.rect.left = screen.get_width() - 50
                    if keys[pygame.K_w] and surface == "game":
                        if Werewolf1.rect.top - velocity > 0:
                            Werewolf1.rect.top -= velocity
                        else:
                            Werewolf1.rect.top = 0
                    if keys[pygame.K_s] and surface == "game":
                        if Werewolf1.rect.top + velocity < screen.get_height():
                            Werewolf1.rect.top += velocity
                        else:
                            Werewolf1.rect.top = screen.get_height() - 50
                    if event.key == pygame.K_SPACE:
                        surface = "game"
                    if surface == "question":
                                if event.key == pygame.K_1:
                                    surface = "game"
                                    if checkCorrectAnswer(
                                        questionType,
                                        1,
                                        questionNumberforCheckEla,
                                        questionNumberforCheckMath,
                                    ):
                                        pass
                                if event.key == pygame.K_2:
                                    surface = "game"
                                    if checkCorrectAnswer(
                                        questionType,
                                        2,
                                        questionNumberforCheckEla,
                                        questionNumberforCheckMath,
                                    ):
                                        pass
                                if event.key == pygame.K_3:
                                    surface = "game"
                                    if checkCorrectAnswer(
                                        questionType,
                                        3,
                                        questionNumberforCheckEla,
                                        questionNumberforCheckMath,
                                    ):
                                        pass
                                if event.key == pygame.K_4:
                                    surface = "game"
                                    if checkCorrectAnswer(
                                        questionType,
                                        4,
                                        questionNumberforCheckEla,
                                        questionNumberforCheckMath,
                                    ):
                                        pass

    if surface == "start screen":
        screen.blit(startScreenText, (200, 400))
        


    if surface == "game":
        screen.blit(GameBackground.image, GameBackground.rect)
        screen.blit(Werewolf1.image, Werewolf1.rect)

        if ElaGhost1Exist:
            screen.blit(ElaGhost1.image, ElaGhost1.rect)
        if ElaGhost2Exist:
            screen.blit(ElaGhost2.image, ElaGhost2.rect)
        if ElaGhost3Exist:
            screen.blit(ElaGhost3.image, ElaGhost3.rect)
        if ElaGhost4Exist:
            screen.blit(ElaGhost4.image, ElaGhost4.rect)
        if ElaGhost5Exist:
            screen.blit(ElaGhost5.image, ElaGhost5.rect)
        if ElaGhost6Exist:
            screen.blit(ElaGhost6.image, ElaGhost6.rect)
        if ElaGhost7Exist:
            screen.blit(ElaGhost7.image, ElaGhost7.rect)

        if MathGhost1Exist:
            screen.blit(MathGhost1.image, MathGhost1.rect)
        if MathGhost2Exist:
            screen.blit(MathGhost2.image, MathGhost2.rect)
        if MathGhost3Exist:
            screen.blit(MathGhost3.image, MathGhost3.rect)
        if MathGhost4Exist:
            screen.blit(MathGhost4.image, MathGhost4.rect)
        if MathGhost5Exist:
            screen.blit(MathGhost5.image, MathGhost5.rect)
        if MathGhost6Exist:
            screen.blit(MathGhost6.image, MathGhost6.rect)
        if MathGhost7Exist:
            screen.blit(MathGhost7.image, MathGhost7.rect)

        if ElaGhost1Exist and pygame.Rect.colliderect(
            Werewolf1.rect, ElaGhost1.rect
        ):
            textQuestion = font.render(
                displayQuestion(questionNumber), True, textColor2
            )
            questionNumber += 15
            textBox1 = textQuestion.get_rect()
            textBox1.center = (400, 400)
            surface = "question"
            ElaGhost1Exist = False
            questionType = "Ela"
            questionNumberforCheckEla += 1

        if ElaGhost2Exist and pygame.Rect.colliderect(
            Werewolf1.rect, ElaGhost2.rect
        ):
            textQuestion = font.render(
                displayQuestion(questionNumber), True, textColor2
            )
            questionNumber += 15
            textBox1 = textQuestion.get_rect()
            textBox1.center = (400, 400)
            surface = "question"
            ElaGhost2Exist = False
            questionType = "Ela"
            questionNumberforCheckEla += 1

        if ElaGhost3Exist and pygame.Rect.colliderect(
            Werewolf1.rect, ElaGhost3.rect
        ):
            textQuestion = font.render(
                displayQuestion(questionNumber), True, textColor2
            )
            questionNumber += 15
            textBox1 = textQuestion.get_rect()
            textBox1.center = (400, 400)
            surface = "question"
            ElaGhost3Exist = False
            questionType = "Ela"
            questionNumberforCheckEla += 1

        if ElaGhost4Exist and pygame.Rect.colliderect(
            Werewolf1.rect, ElaGhost4.rect
        ):
            textQuestion = font.render(
                displayQuestion(questionNumber), True, textColor2
            )
            questionNumber += 15
            textBox1 = textQuestion.get_rect()
            textBox1.center = (400, 400)
            surface = "question"
            ElaGhost4Exist = False
            questionType = "Ela"
            questionNumberforCheckEla += 1

        if ElaGhost5Exist and pygame.Rect.colliderect(
            Werewolf1.rect, ElaGhost5.rect
        ):
            textQuestion = font.render(
                displayQuestion(questionNumber), True, textColor2
            )
            questionNumber += 15
            textBox1 = textQuestion.get_rect()
            textBox1.center = (400, 400)
            surface = "question"
            ElaGhost5Exist = False
            questionType = "Ela"
            questionNumberforCheckEla += 1

        if ElaGhost6Exist and pygame.Rect.colliderect(
            Werewolf1.rect, ElaGhost6.rect
        ):
            textQuestion = font.render(
                displayQuestion(questionNumber), True, textColor2
            )
            questionNumber += 15
            textBox1 = textQuestion.get_rect()
            textBox1.center = (400, 400)
            surface = "question"
            ElaGhost6Exist = False
            questionType = "Ela"
            questionNumberforCheckEla += 1

        if ElaGhost7Exist and pygame.Rect.colliderect(
            Werewolf1.rect, ElaGhost7.rect
        ):
            textQuestion = font.render(
                displayQuestion(questionNumber), True, textColor2
            )
            questionNumber += 15
            textBox1 = textQuestion.get_rect()
            textBox1.center = (400, 400)
            surface = "question"
            ElaGhost7Exist = False
            questionType = "Ela"
            questionNumberforCheckEla += 1

        if MathGhost1Exist and pygame.Rect.colliderect(
            Werewolf1.rect, MathGhost1.rect
        ):
            textQuestion = font.render(
                displayQuestionm(questionNumberm), True, textColor2
            )
            questionNumberm += 8
            textBox1 = textQuestion.get_rect()
            textBox1.center = (400, 400)
            surface = "question"
            MathGhost1Exist = False
            questionType = "Math"
            questionNumberforCheckMath += 1

        if MathGhost2Exist and pygame.Rect.colliderect(
            Werewolf1.rect, MathGhost2.rect
        ):
            textQuestion = font.render(
                displayQuestionm(questionNumberm), True, textColor2
            )
            questionNumberm += 8
            textBox1 = textQuestion.get_rect()
            textBox1.center = (400, 400)
            surface = "question"
            MathGhost2Exist = False
            questionType = "Math"
            questionNumberforCheckMath += 1

        if MathGhost3Exist and pygame.Rect.colliderect(
            Werewolf1.rect, MathGhost3.rect
        ):
            textQuestion = font.render(
                displayQuestionm(questionNumberm), True, textColor2
            )
            questionNumberm += 8
            textBox1 = textQuestion.get_rect()
            textBox1.center = (400, 400)
            surface = "question"
            MathGhost3Exist = False
            questionType = "Math"
            questionNumberforCheckMath += 1

        if MathGhost4Exist and pygame.Rect.colliderect(
            Werewolf1.rect, MathGhost4.rect
        ):
            textQuestion = font.render(
                displayQuestionm(questionNumberm), True, textColor2
            )
            questionNumberm += 8
            textBox1 = textQuestion.get_rect()
            textBox1.center = (400, 400)
            surface = "question"
            MathGhost4Exist = False
            questionType = "Math"
            questionNumberforCheckMath += 1

        if MathGhost5Exist and pygame.Rect.colliderect(
            Werewolf1.rect, MathGhost5.rect
        ):
            textQuestion = font.render(
                displayQuestionm(questionNumberm), True, textColor2
            )
            questionNumberm += 8
            textBox1 = textQuestion.get_rect()
            textBox1.center = (400, 400)
            surface = "question"
            MathGhost5Exist = False
            questionType = "Math"
            questionNumberforCheckMath += 1

        if MathGhost6Exist and pygame.Rect.colliderect(
            Werewolf1.rect, MathGhost6.rect
        ):
            textQuestion = font.render(
                displayQuestionm(questionNumberm), True, textColor2
            )
            questionNumberm += 8
            textBox1 = textQuestion.get_rect()
            textBox1.center = (400, 400)
            surface = "question"
            MathGhost6Exist = False
            questionType = "Math"
            questionNumberforCheckMath += 1

        if MathGhost7Exist and pygame.Rect.colliderect(
            Werewolf1.rect, MathGhost7.rect
        ):
            textQuestion = font.render(
                displayQuestionm(questionNumberm), True, textColor2
            )
            questionNumberm += 8
            textBox1 = textQuestion.get_rect()
            textBox1.center = (400, 400)
            surface = "question"
            MathGhost7Exist = False
            questionType = "Math"
            questionNumberforCheckMath += 1

    if surface == "question":
        screen.fill((255, 255, 255))
        screen.blit(textQuestion, textBox1)

    if (
        not MathGhost1Exist
        and not MathGhost2Exist
        and not MathGhost3Exist
        and not MathGhost4Exist
        and not MathGhost5Exist
        and not MathGhost6Exist
        and not MathGhost7Exist
        and not ElaGhost1Exist
        and not ElaGhost2Exist
        and not ElaGhost3Exist
        and not ElaGhost4Exist
        and not ElaGhost5Exist
        and not ElaGhost6Exist
        and not ElaGhost7Exist
        and surface == "game"
    ):
        screen.blit(ExitDoor.image, ExitDoor.rect)
        if pygame.Rect.colliderect(Werewolf1.rect, ExitDoor.rect):
            surface = "end"

    if surface == "end":
        screen.fill((255, 255, 255))
        text = font.render(
            f"Congrats you escaped! Your score was {score}/14", True, (0, 0, 0)
        )
        screen.blit(text, (200, 400))
        with open(
                    "/Users/saisirasapalli/IdeaProjects/IB Computer Science SL Projects/Congressional App Challenge/score.txt",
                    "w",
                ) as w:
                    w.write(str(score))

        

        
    pygame.display.update()
    clock.tick(60)

pygame.quit()