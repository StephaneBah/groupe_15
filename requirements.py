def get_requirements():
    return [
        'Pillow==9.2.0',
        'diffusers',
    ]

if __name__ == '__main__':
    requirements = get_requirements()
    for req in requirements:
        print(req)
