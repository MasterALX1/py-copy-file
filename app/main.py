def copy_file(command: str) -> None:
    if not command.startswith("cp "):
        return
    try:
        source_file = command.split(" ")[1]
        destination_file = command.split(" ")[2]
        if source_file == destination_file:
            return
        with (
            open(source_file, "r") as file_in,
            open(destination_file, "w") as file_out,
        ):
            file_out.write(file_in.read())
    except Exception:
        return
