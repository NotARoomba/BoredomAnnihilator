{ pkgs }: {
    deps = [
      pkgs.sudo
      pkgs.python39Packages.poetry
      pkgs.python39Packages.pip
      pkgs.python39Full
    ];
}