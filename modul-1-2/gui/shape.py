import customtkinter

from math import pi, sqrt

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


class Shape:
    class Two:
        class Square:
            def area(length: float) -> float:
                return length**2

            def perimeter(length: float) -> float:
                return length * 4

        class Rectangle:
            def area(length: float, width: float) -> float:
                return length * width

            def perimeter(length: float, width: float) -> float:
                return 2 * (length + width)

    class Three:
        class Cube:
            def volume(length: float) -> float:
                return length**3

            def surfaceArea(length: float) -> float:
                return 6 * (length**2)

        class Cuboid:
            def volume(length: float, width: float, height: float) -> float:
                return length * width * height

            def surfaceArea(length: float, width: float, height: float) -> float:
                return 2 * (length * width + length * height + width * height)

        class Cone:
            def volume(radius: float, height: float) -> float:
                return (1 / 3) * pi * (radius**2) * height

            def surfaceArea(radius: float, height: float) -> float:
                return pi * radius * (radius + (sqrt(radius**2 + height**2)))

        class Sphere:
            def volume(radius: float) -> float:
                return (4 / 3) * pi * (radius**3)

            def surfaceArea(radius: float) -> float:
                return 4 * pi * (radius**2)

        class Cylinder:
            def volume(radius: float, height: float) -> float:
                return pi * (radius**2) * height

            def surfaceArea(radius: float, height: float) -> float:
                return 2 * pi * radius * (radius + height)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.shapeChoice = {"2D": "Square", "3D": "Cube"}

        self.title("Shape Calculator")
        self.geometry(f"{400}x{600}")
        self.resizable(width=False, height=False)

        self.mainFrame = customtkinter.CTkFrame(self)
        self.mainFrame.pack(pady=20, padx=20, fill="both", expand=True)

        self.dimensionSegmented = customtkinter.CTkSegmentedButton(
            self.mainFrame,
            command=self.switchShapeDimension,
            values=["2D", "3D"],
            font=customtkinter.CTkFont(size=14, weight="bold"),
        )
        self.dimensionSegmented.set("2D")
        self.dimensionSegmented.pack(pady=10, padx=10, fill="both")

        self.shapeOption = customtkinter.CTkOptionMenu(
            self.mainFrame,
            command=self.shapeOptionEvent,
            values=["Square", "Rectangle", "Triangle", "Circle"],
            font=customtkinter.CTkFont(size=14, weight="bold"),
        )
        self.shapeOption.set("Square")
        self.shapeOption.pack(pady=10, padx=10, fill="both")

        self.lengthLabel = customtkinter.CTkLabel(
            self.mainFrame,
            text="Length: ",
            font=customtkinter.CTkFont(size=14, weight="bold"),
            anchor="w",
        )
        self.lengthEntry = customtkinter.CTkEntry(
            self.mainFrame,
            placeholder_text="Insert length here",
            font=customtkinter.CTkFont(size=12, weight="bold"),
        )

        self.component2D()
        self.component3D()
        self.defaultShapeDimension()

    def component2D(self):
        self.areaEntryText = customtkinter.StringVar()
        self.areaLabel = customtkinter.CTkLabel(
            self.mainFrame,
            text="Area",
            font=customtkinter.CTkFont(size=16, weight="bold"),
        )
        self.areaEntry = customtkinter.CTkEntry(
            self.mainFrame,
            font=customtkinter.CTkFont(size=14, weight="bold"),
            textvariable=self.areaEntryText,
            state="disabled",
        )

        self.perimeterEntryText = customtkinter.StringVar()
        self.perimeterLabel = customtkinter.CTkLabel(
            self.mainFrame,
            text="Perimeter",
            font=customtkinter.CTkFont(size=16, weight="bold"),
        )
        self.perimeterEntry = customtkinter.CTkEntry(
            self.mainFrame,
            font=customtkinter.CTkFont(size=14, weight="bold"),
            textvariable=self.perimeterEntryText,
            state="disabled",
        )

    def component3D(self):
        self.volumeEntryText = customtkinter.StringVar()
        self.volumeLabel = customtkinter.CTkLabel(
            self.mainFrame,
            text="Volume",
            font=customtkinter.CTkFont(size=16, weight="bold"),
        )
        self.volumeEntry = customtkinter.CTkEntry(
            self.mainFrame,
            font=customtkinter.CTkFont(size=14, weight="bold"),
            textvariable=self.volumeEntryText,
            state="disabled",
        )

        self.surfaceAreaEntryText = customtkinter.StringVar()
        self.surfaceAreaLabel = customtkinter.CTkLabel(
            self.mainFrame,
            text="Surface Area",
            font=customtkinter.CTkFont(size=16, weight="bold"),
        )
        self.surfaceAreaEntry = customtkinter.CTkEntry(
            self.mainFrame,
            font=customtkinter.CTkFont(size=14, weight="bold"),
            textvariable=self.surfaceAreaEntryText,
            state="disabled",
        )

    def defaultShapeDimension(self):
        self.shapeDimension = 2
        self.show2D()

    def switchShapeDimension(self, value):
        if value == "2D":
            self.shapeOption.configure(
                values=["Square", "Rectangle", "Triangle", "Circle"]
            )
            self.shapeOption.set(self.shapeChoice["2D"])

            self.show2D()
            self.shapeDimension = 2

        else:
            self.shapeOption.configure(
                values=[
                    "Cube",
                    "Cuboid",
                    "Cone",
                    "Sphere",
                    "Cylinder",
                ]
            )
            self.shapeOption.set(self.shapeChoice["3D"])

            self.show3D()
            self.shapeDimension = 3

    def show2D(self):
        self.volumeLabel.pack_forget()
        self.volumeEntry.pack_forget()
        self.surfaceAreaLabel.pack_forget()
        self.surfaceAreaEntry.pack_forget()

        self.areaLabel.pack(pady=(40, 0), padx=10, fill="both")
        self.areaEntry.pack(padx=10, fill="both")
        self.perimeterLabel.pack(pady=(10, 0), padx=10, fill="both")
        self.perimeterEntry.pack(padx=10, fill="both")

    def show3D(self):
        self.areaLabel.pack_forget()
        self.areaEntry.pack_forget()
        self.perimeterLabel.pack_forget()
        self.perimeterEntry.pack_forget()

        self.volumeLabel.pack(pady=(40, 0), padx=10, fill="both")
        self.volumeEntry.pack(padx=10, fill="both")
        self.surfaceAreaLabel.pack(pady=(10, 0), padx=10, fill="both")
        self.surfaceAreaEntry.pack(padx=10, fill="both")

    def shapeOptionEvent(self, value):
        if self.shapeDimension == 2:
            self.shapeChoice["2D"] = value

        else:
            self.shapeChoice["3D"] = value


if __name__ == "__main__":
    app = App()
    app.mainloop()
