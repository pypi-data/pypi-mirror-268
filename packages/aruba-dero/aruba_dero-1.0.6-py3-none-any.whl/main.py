import os
import sys

from bullet import colors, Bullet

from Module import get_module_names, load_module, Module, get_modules


def main():
    available_modules = get_modules()
    available_modules.append({"name": "Exit"})

    while True:
        cli = Bullet(
            prompt="\nWhich module do you want to use: ",
            choices=get_module_names(available_modules),
            indent=0,
            align=5,
            margin=2,
            bullet="*",
            bullet_color=colors.bright(colors.foreground["cyan"]),
            word_color=colors.bright(colors.foreground["yellow"]),
            word_on_switch=colors.bright(colors.foreground["yellow"]),
            background_color=colors.background["black"],
            background_on_switch=colors.background["black"],
            pad_right=5,
            return_index=True
        )
        selected_module = cli.launch()  # Tuple (name, index)
        # Check for Exit knowing Exit is always the last option
        if selected_module[1] == len(available_modules) - 1:
            exit(0)

        selected_module = available_modules[selected_module[1]]

        # Loads selected module for use and creates module instance
        print(f"Enabling Module: {selected_module.get('name')}")
        print(f"by: {selected_module.get('author')} // {selected_module.get('author_email')}")

        abs_module_path = str(os.path.join(selected_module.get("dir"), selected_module.get("module_file")))
        rel_module_path = str(os.path.relpath(abs_module_path, os.path.dirname(__file__)))

        module_class = load_module(rel_module_path)
        module = module_class()

        try:
            start_module_routine(module)
        except KeyboardInterrupt:
            print("\nAborting...")
            main()
        # utils.stop_webserver(webserver_process)  # Always kill the webserver even when an error occurred


def start_module_routine(module: Module):
    if not module.setup():
        print("ERROR: Setup failed. Exiting...")
        return

    if not module.has_credentials():
        module.ask_credentials()

    if not module.pre_run():
        print("ERROR: Pre-run failed. Exiting...")
        return

    if not module.run():
        print("ERROR: Run failed. Exiting...")
        return

    if not module.post_run():
        print(
            "ERROR: Post-run failed. This means all actions were executed but the cleanup failed. Please investigate manually! Exiting...")
        return

    print("\nReturning to menu.")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
