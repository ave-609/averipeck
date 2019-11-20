import arcade
import random

# --- Constants ---
SPRITE_SCALING_BOX = 0.505
SPRITE_SCALING_DESK = .020
SPRITE_SCALING_PLAYER = 0.058
SPRITE_SCALING_KID = .070
SPRITE_SCALING_AIRPLANE = .013

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MOVEMENT_SPEED = 5

VIEWPORT_MARGIN = 150

PLANE_COUNT = 12
HOMEWORK_COUNT = 5

class Plane(arcade.Sprite):

    def __init__(self, graphic, scaling):

        super().__init__(graphic, scaling)
        self.change_x = 0
        self.change_y = 0

    def reset(self):
        self.bottom = SCREEN_HEIGHT + random.randrange(300)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):

        # Move the image
        self.center_x += self.change_x
        self.center_y += self.change_y

        # If we are out-of-bounds, then 'bounce'
        if (self.left - 64) < 0:
            self.change_x *= -1

        if (self.right + 64) > SCREEN_WIDTH:
            self.change_x *= -1

        if (self.bottom - 64) < 0:
            self.change_y *= -1

        if (self.top + 64) > SCREEN_HEIGHT:
            self.change_y *= -1


class MyGame(arcade.Window):
    """ This class represents the main window of the game. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprites With Walls Example")

        self.player_list = None
        self.wall_list = None
        self.homework_list = None
        self.plane_list = None

        self.player_sprite = None

        self.physics_engine = None

        self.view_left = 0
        self.view_bottom = 0

        self.plane_sound = arcade.load_sound("hurt2.wav")
        self.homework_sound = arcade.load_sound("coin1.wav")

        self.level = 0

    def setup_instructions(self):

        arcade.set_background_color(arcade.color.BLACK)

        self.score = 0

        self.view_left = 0
        self.view_bottom = 0

        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.homework_list = arcade.SpriteList()
        self.plane_list = arcade.SpriteList()

        # image from Pin Clipart(pinclipart.com)
        self.player_sprite = arcade.Sprite("guyteacher.png", .1)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 96
        self.player_list.append(self.player_sprite)

        # image from Pin Clipart(pinclipart.com)
        self.homework_sprite = arcade.Sprite("homework2.png", 0.12)
        self.homework_sprite.center_x = 500
        self.homework_sprite.center_y = 96
        self.homework_list.append(self.homework_sprite)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

    def setup_level_1(self):
        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)
        self.level = 1

        self.score = 0

        self.view_left = 0
        self.view_bottom = 0

        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.homework_list = arcade.SpriteList()
        self.plane_list = arcade.SpriteList()

        # image from pinclipart.com
        self.player_sprite = arcade.Sprite("guyteacher.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 164
        self.player_sprite.center_y = 96
        self.player_list.append(self.player_sprite)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        for x in range(192, 1300, 145):
            # image from Pin Clipart (pinclipart.com)
            wall = arcade.Sprite("Desks.png", SPRITE_SCALING_DESK)
            wall.center_x = x
            wall.center_y = 300
            self.wall_list.append(wall)

        for i in range(2):
            # image from Pin Clipart (pinclipart.com)
            wall = arcade.Sprite("Desks.png", SPRITE_SCALING_DESK)
            wall.center_x = i * 64 + 148
            wall.center_y = 160
            self.wall_list.append(wall)

        for i in range(3):
            # image from Pin Clipart (pinclipart.com)
            wall = arcade.Sprite("Desks.png", SPRITE_SCALING_DESK)
            wall.center_x = i * 64 + 340
            wall.center_y = 160
            self.wall_list.append(wall)

        wall = arcade.Sprite("kid.png", SPRITE_SCALING_KID)
        wall.center_x = i * 64 + 404
        wall.center_y = 160
        self.wall_list.append(wall)

        for i in range(2):
            wall = arcade.Sprite("Desks.png", SPRITE_SCALING_DESK)
            wall.center_x = i * 64 + 660
            wall.center_y = 160
            self.wall_list.append(wall)

        wall = arcade.Sprite("kid.png", SPRITE_SCALING_KID)
        wall.center_x = i * 64 + 788
        wall.center_y = 160
        self.wall_list.append(wall)

        for i in range(3):
            wall = arcade.Sprite("Desks.png", SPRITE_SCALING_DESK)
            wall.center_x = i * 64 + 916
            wall.center_y = 160
            self.wall_list.append(wall)

        wall = arcade.Sprite("kid.png", SPRITE_SCALING_KID)
        wall.center_x = 1172
        wall.center_y = 160
        self.wall_list.append(wall)

        for i in range(3):
            wall = arcade.Sprite("Desks.png", SPRITE_SCALING_DESK)
            wall.center_x = i * 64 + 148
            wall.center_y = 448
            self.wall_list.append(wall)

        wall = arcade.Sprite("kid.png", SPRITE_SCALING_KID)
        wall.center_x = i * 64 + 212
        wall.center_y = 448
        self.wall_list.append(wall)

        for i in range(2):
            wall = arcade.Sprite("Desks.png", SPRITE_SCALING_DESK)
            wall.center_x = i * 64 + 468
            wall.center_y = 448
            self.wall_list.append(wall)

        wall = arcade.Sprite("kid.png", SPRITE_SCALING_KID)
        wall.center_x = i * 64 + 596
        wall.center_y = 448
        self.wall_list.append(wall)

        for i in range(3):
            wall = arcade.Sprite("Desks.png", SPRITE_SCALING_DESK)
            wall.center_x = i * 64 + 724
            wall.center_y = 448
            self.wall_list.append(wall)

        for i in range(2):
            wall = arcade.Sprite("Desks.png", SPRITE_SCALING_DESK)
            wall.center_x = i * 64 + 980
            wall.center_y = 448
            self.wall_list.append(wall)

        wall = arcade.Sprite("kid.png", SPRITE_SCALING_KID)
        wall.center_x = 1172
        wall.center_y = 448
        self.wall_list.append(wall)


        # Outside walls
        for i in range(20):
            # image from kenny.nl
            wall = arcade.Sprite("grassCenter_round.png", SPRITE_SCALING_BOX)
            wall.center_x = i * 64 + 84
            wall.center_y = 32
            self.wall_list.append(wall)

        for i in range(20):
            wall = arcade.Sprite("grassCenter_round.png", SPRITE_SCALING_BOX)
            wall.center_x = i * 64 + 84
            wall.center_y = 608
            self.wall_list.append(wall)

        for i in range(9):
            wall = arcade.Sprite("grassCenter_round.png", SPRITE_SCALING_BOX)
            wall.center_x = 1300
            wall.center_y = i * 64 + 32
            self.wall_list.append(wall)

        for i in range(9):
            wall = arcade.Sprite("grassCenter_round.png", SPRITE_SCALING_BOX)
            wall.center_x = 84
            wall.center_y = i * 64 + 32
            self.wall_list.append(wall)


        for i in range(HOMEWORK_COUNT):
            # image from Pin Clipart(pinclipart.com)
            homework = arcade.Sprite("homework2.png", 0.032)

            homework_placed_successfully = False
            while not homework_placed_successfully:

                homework.center_x = random.randrange(192, 1000)
                homework.center_y = random.randrange(64, 600)

                wall_hit_list = arcade.check_for_collision_with_list(homework, self.wall_list)
                homework_hit_list = arcade.check_for_collision_with_list(homework, self.homework_list)
                if len(wall_hit_list) == 0 and len(homework_hit_list) == 0:
                    homework_placed_successfully = True
            self.homework_list.append(homework)

        for i in range(PLANE_COUNT):

            # image from Pin Clipart (pinclipart.com)
            plane = Plane("airplane.png", SPRITE_SCALING_AIRPLANE)

            # Position the plane
            plane.center_x = random.randrange(234, 1200)
            plane.center_y = random.randrange(234, 534)
            while plane.change_x == 0 and plane.change_y == 0:
                plane.change_x = random.randrange(-3, 4)
                plane.change_y = random.randrange(-3, 4)

            # Add the plane to the list
            self.plane_list.append(plane)

    def setup_level_2(self):
        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

        self.level = 2

        self.view_left = 0
        self.view_bottom = 0

        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.homework_list = arcade.SpriteList()
        self.plane_list = arcade.SpriteList()

        # image from pinclipart.com
        self.player_sprite = arcade.Sprite("guyteacher.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 164
        self.player_sprite.center_y = 96
        self.player_list.append(self.player_sprite)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        for x in range(192, 1300, 145):
            # image from Pin Clipart (pinclipart.com)
            wall = arcade.Sprite("Desks.png", SPRITE_SCALING_DESK)
            wall.center_x = x
            wall.center_y = 300
            self.wall_list.append(wall)

        for i in range(2):
            # image from Pin Clipart (pinclipart.com)
            wall = arcade.Sprite("Desks.png", SPRITE_SCALING_DESK)
            wall.center_x = i * 64 + 148
            wall.center_y = 160
            self.wall_list.append(wall)

        for i in range(3):
            # image from Pin Clipart (pinclipart.com)
            wall = arcade.Sprite("Desks.png", SPRITE_SCALING_DESK)
            wall.center_x = i * 64 + 340
            wall.center_y = 160
            self.wall_list.append(wall)

        wall = arcade.Sprite("kid.png", SPRITE_SCALING_KID)
        wall.center_x = i * 64 + 404
        wall.center_y = 160
        self.wall_list.append(wall)

        for i in range(2):
            wall = arcade.Sprite("Desks.png", SPRITE_SCALING_DESK)
            wall.center_x = i * 64 + 660
            wall.center_y = 160
            self.wall_list.append(wall)

        wall = arcade.Sprite("kid.png", SPRITE_SCALING_KID)
        wall.center_x = i * 64 + 788
        wall.center_y = 160
        self.wall_list.append(wall)

        for i in range(3):
            wall = arcade.Sprite("Desks.png", SPRITE_SCALING_DESK)
            wall.center_x = i * 64 + 916
            wall.center_y = 160
            self.wall_list.append(wall)

        wall = arcade.Sprite("kid.png", SPRITE_SCALING_KID)
        wall.center_x = 1172
        wall.center_y = 160
        self.wall_list.append(wall)

        for i in range(3):
            wall = arcade.Sprite("Desks.png", SPRITE_SCALING_DESK)
            wall.center_x = i * 64 + 148
            wall.center_y = 448
            self.wall_list.append(wall)

        wall = arcade.Sprite("kid.png", SPRITE_SCALING_KID)
        wall.center_x = i * 64 + 212
        wall.center_y = 448
        self.wall_list.append(wall)

        for i in range(2):
            wall = arcade.Sprite("Desks.png", SPRITE_SCALING_DESK)
            wall.center_x = i * 64 + 468
            wall.center_y = 448
            self.wall_list.append(wall)

        wall = arcade.Sprite("kid.png", SPRITE_SCALING_KID)
        wall.center_x = i * 64 + 596
        wall.center_y = 448
        self.wall_list.append(wall)

        for i in range(3):
            wall = arcade.Sprite("Desks.png", SPRITE_SCALING_DESK)
            wall.center_x = i * 64 + 724
            wall.center_y = 448
            self.wall_list.append(wall)

        for i in range(2):
            wall = arcade.Sprite("Desks.png", SPRITE_SCALING_DESK)
            wall.center_x = i * 64 + 980
            wall.center_y = 448
            self.wall_list.append(wall)

        wall = arcade.Sprite("kid.png", SPRITE_SCALING_KID)
        wall.center_x = 1172
        wall.center_y = 448
        self.wall_list.append(wall)


        # Outside walls
        for i in range(20):
            # image from kenny.nl
            wall = arcade.Sprite("grassCenter_round.png", SPRITE_SCALING_BOX)
            wall.center_x = i * 64 + 84
            wall.center_y = 32
            self.wall_list.append(wall)

        for i in range(20):
            wall = arcade.Sprite("grassCenter_round.png", SPRITE_SCALING_BOX)
            wall.center_x = i * 64 + 84
            wall.center_y = 608
            self.wall_list.append(wall)

        for i in range(9):
            wall = arcade.Sprite("grassCenter_round.png", SPRITE_SCALING_BOX)
            wall.center_x = 1300
            wall.center_y = i * 64 + 32
            self.wall_list.append(wall)

        for i in range(9):
            wall = arcade.Sprite("grassCenter_round.png", SPRITE_SCALING_BOX)
            wall.center_x = 84
            wall.center_y = i * 64 + 32
            self.wall_list.append(wall)


        for i in range(HOMEWORK_COUNT):
            # image from Pin Clipart(pinclipart.com)
            homework = arcade.Sprite("homework2.png", 0.032)

            homework_placed_successfully = False
            while not homework_placed_successfully:

                homework.center_x = random.randrange(192, 1000)
                homework.center_y = random.randrange(64, 600)

                wall_hit_list = arcade.check_for_collision_with_list(homework, self.wall_list)
                homework_hit_list = arcade.check_for_collision_with_list(homework, self.homework_list)
                if len(wall_hit_list) == 0 and len(homework_hit_list) == 0:
                    homework_placed_successfully = True
            self.homework_list.append(homework)

        for i in range(PLANE_COUNT):

            # image from Pin Clipart (pinclipart.com)
            plane = Plane("airplane.png", SPRITE_SCALING_AIRPLANE)

            # Position the plane
            plane.center_x = random.randrange(234, 1200)
            plane.center_y = random.randrange(234, 534)
            while plane.change_x == 0 and plane.change_y == 0:
                plane.change_x = random.randrange(-3, 4)
                plane.change_y = random.randrange(-3, 4)

            # Add the plane to the list
            self.plane_list.append(plane)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if len(self.homework_list) != 0 and len(self.plane_list) != 0:
            if key == arcade.key.UP:
                self.player_sprite.change_y = MOVEMENT_SPEED
            elif key == arcade.key.DOWN:
                self.player_sprite.change_y = -MOVEMENT_SPEED
            elif key == arcade.key.LEFT:
                self.player_sprite.change_x = -MOVEMENT_SPEED
            elif key == arcade.key.RIGHT:
                self.player_sprite.change_x = MOVEMENT_SPEED
        if key == arcade.key.SPACE:
                self.level += 1

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0
        if key == arcade.key.SPACE:
            self.level -= 1

    def on_draw(self):
        arcade.start_render()

        if self.level != 0:
            self.wall_list.draw()
            self.player_list.draw()
            self.homework_list.draw()
            self.plane_list.draw()

            output = f"Homework Collected: {self.score}"
            arcade.draw_text(output, self.view_left + VIEWPORT_MARGIN - 128, self.view_bottom +
                             VIEWPORT_MARGIN - 128, arcade.color.WHITE, 14)

            if len(self.homework_list) == 0:
                arcade.draw_text("Game Over!", self.view_left + VIEWPORT_MARGIN + 128, self.view_bottom +
                             VIEWPORT_MARGIN + 128, arcade.color.BLACK, 60)

            elif len(self.plane_list) == 0:
                arcade.draw_text("You Lose!", self.view_left + VIEWPORT_MARGIN + 128, self.view_bottom +
                             VIEWPORT_MARGIN + 128, arcade.color.BLACK, 60)
        else:
            arcade.draw_text("Homework Collector ",
                             self.view_left + VIEWPORT_MARGIN - 50, self.view_bottom +
                             VIEWPORT_MARGIN + 220, arcade.color.AMAZON, 60)
            arcade.draw_text("Homework Collector ",
                             self.view_left + VIEWPORT_MARGIN - 55, self.view_bottom +
                             VIEWPORT_MARGIN + 219, arcade.color.WHITE, 60)
            arcade.draw_text("Your students are throwing paper airplanes around the classroom. ",
                             self.view_left + VIEWPORT_MARGIN + 20, self.view_bottom +
                             VIEWPORT_MARGIN + 175, arcade.color.WHITE, 15)
            arcade.draw_text("Collect your students homework without getting hit!",
                             self.view_left + VIEWPORT_MARGIN + 70, self.view_bottom +
                             VIEWPORT_MARGIN + 150, arcade.color.WHITE, 15)
            arcade.draw_text(
                "If all the paper airplanes hit you, you loose the game.",
                self.view_left + VIEWPORT_MARGIN + 67, self.view_bottom +
                VIEWPORT_MARGIN + 125, arcade.color.WHITE, 15)
            arcade.draw_text(
                "Press the space bar to continue.",
                self.view_left + VIEWPORT_MARGIN + 145, self.view_bottom +
                VIEWPORT_MARGIN + 35, arcade.color.WHITE, 15)
            self.player_list.draw()
            self.homework_list.draw()
        if self.level == 1:
            arcade.draw_text(
                "Level 1",
                self.view_left + VIEWPORT_MARGIN + 500, self.view_bottom +
                VIEWPORT_MARGIN - 128, arcade.color.WHITE, 25)
        if self.level == 2:
            arcade.draw_text(
                "Level 2",
                self.view_left + VIEWPORT_MARGIN + 500, self.view_bottom +
                VIEWPORT_MARGIN - 128, arcade.color.WHITE, 25)

    def on_update(self, delta_time):
        self.physics_engine.update()

        changed = False

        left_boundary = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        right_boundary = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        top_boundary = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        bottom_boundary = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        self.view_left = int(self.view_left)
        self.view_bottom = int(self.view_bottom)

        if changed:
            arcade.set_viewport(self.view_left, self.view_left + SCREEN_WIDTH - 1,
                                self.view_bottom, self.view_bottom + SCREEN_HEIGHT - 1)

        if len(self.homework_list) != 0 and len(self.plane_list) != 0:
            self.homework_list.update()

        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.homework_list)

        for homework in hit_list:
            homework.remove_from_sprite_lists()
            arcade.play_sound(self.homework_sound)
            self.score += 1

        if len(self.plane_list) != 0 and len(self.homework_list) != 0:
            self.plane_list.update()

        plane_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.plane_list)

        for plane in plane_hit_list:
            plane.remove_from_sprite_lists()
            arcade.play_sound(self.plane_sound)
            self.score -= 1

        if len(self.homework_list) == 0 and self.level == 1:
            self.setup_level_2()





def main():
    window = MyGame()
    window.setup_instructions()
    arcade.run()



if __name__ == "__main__":
    main()