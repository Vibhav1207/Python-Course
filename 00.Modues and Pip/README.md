<div align="center">
  <img src="">
</div>

---
# 🐍 Python Modules and pip

Welcome to the Python Modules and pip section! In this section, you'll learn about the modules, types of modules and pip you can use in Python. 

## 📚 Table of Contents

- [Modules](#-modules)
- [pip](#-the-pip-command)

## 🫙 Modules

Modules are like libraries that you can use in your Python code. They contain pre-written functions and classes that you can use to perform various tasks. You can import modules into your code using the `import` statement.

## Types of modules 

- **Built-in modules**: These are modules that come pre-installed with Python. You don't need to install them separately. Examples include `math`, `random`, and `time`.

- **External modules**: These are modules that you need to install separately using pip. Examples include `requests` , `pyttsx3` , ` pandas `. 

## 📦 The pip command

Pip is a package management system used to install and manage software packages written in Python. It simplifies the process of installing and managing libraries and dependencies in Python projects.

## Key Features

- **Installation of Packages**: Pip allows you to install packages from the Python Package Index (PyPI) and other package indexes.
- **Dependency Management**: Pip automatically installs any dependencies required by the package you're installing.
- **Upgrading Packages**: Pip can upgrade installed packages to the latest versions available.
- **Uninstalling Packages**: Pip can also uninstall packages that are no longer needed.
- **Requirements Files**: Pip can install all the packages listed in a requirements file, which is a plain text file that contains a list of package names and versions.

## Basic Commands

- **Install a package**:
  ```bash
  pip install package_name #Replace package_name with module name eg. pyttsx3 (pip install pyttsx3) 
  ```
 
- **Upgrade a package**:
```bash 
 pip install --upgrade package_name #Replace package_name with module name eg. pyttsx3 (pip install --upgrade pyttsx3)
```
- **Uninstall a package**:
```bash 
 pip uninstall package_name #Replace package_name with module name eg. pyttsx3 (pip uninstall pyttsx3)
 ```

- **List installed packages**:
```bash
pip list
```

- **Show information about a package**:
```bash 
pip show package_name #Replace package_name with module name eg. pyttsx3 (pip show pyttsx3)
```

- **Install packages from a requirements file**: 
```bash 
pip install -r requirements.txt #Important command if you want to install all the packages listed in a requirements file at once
```
