async def run(hub):
    """
    Initialize the "hub" cli.

    .. code-block:: bash

        hub <ref> positional1 positional2 --flag1 --flag2 --key1=value --key2 value \
            --list="a,b,c" --json="{'a': 'b'}" --flag3

    Args:
        hub (pop.hub.Hub): The global namespace
    """
    # Grab OPT for cli, arguments it doesn't use will be passed onward to the next cli
    opt = hub.lib.cpop.data.NamespaceDict(hub.OPT.copy())
    ref = opt.cli.ref
    await hub.log.debug(f"Using ref: hub.{ref}")

    # If no cli was defined, then use the first part of the passed ref as the authoritative cli
    cli = opt.cli.cli or ref.split(".")[0]
    await hub.log.debug(f"Using cli: {cli}")

    # Try to restore the hub state
    hub_state_file = await hub.cli.state.restore(opt)

    if opt.cli.cli or (
        (cli in hub._dynamic.config.cli_config) and (cli not in opt.get("pop", {}).get("global_clis", ()))
    ):
        await hub.log.debug(f"Loading cli: {cli}")
        # Reload hub.OPT with the cli arguments not consumed by the initial hub
        await hub.cli.config.override(cli, opt)
        args = []
        kwargs = {}
    else:
        # Treat all the extra args as parameters for the named ref
        args, kwargs = await hub.cli.cli.parameters(opt)
        await hub.log.debug(f"Args: {' '.join(args)}")
        await hub.log.debug(f"Kwargs: {' '.join(kwargs.keys())}")

    # Get the named reference from the hub
    finder = hub.lib.cpop.ref.find(hub, ref)

    # Call or retrieve the object at the given ref
    ret = await hub.cli.ref.resolve(finder, *args, **kwargs)

    # output the results of finder to the console
    await hub.cli.ref.output(ret)

    if opt.cli.interactive:
        # Start an asynchronous interactive console
        await hub.cli.console.run(opt=opt, ref=finder)

    if hub_state_file:
        # Write the serialized hub to a file
        hub_state_file = await hub.cli.state.save(hub_state_file)
