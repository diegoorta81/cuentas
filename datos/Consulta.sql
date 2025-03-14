

CREATE TABLE IF NOT EXISTS `t_tiposcuenta` (
  `id` integer PRIMARY KEY autoincrement,
  `tipo` varchar(100) NOT NULL
);

INSERT INTO `t_tiposcuenta` (`id`, `tipo`) VALUES
	(1, 'ACTIVO'),
	(2, 'PASIVO');



CREATE TABLE "t_cuentas" (
	"id" INTEGER NOT NULL,
	"fecha_ini" UNKNOWN NOT NULL,
	"cuenta" VARCHAR(90) NOT NULL,
	"fecha_mod" UNKNOWN NULL,
	"id_padre" INTEGER NULL,
	"id_tipo" INTEGER NOT NULL,
	"orden" INTEGER NULL,
	"limite" REAL NULL,
	PRIMARY KEY ("id"),
	CONSTRAINT "0" FOREIGN KEY ("id_tipo") REFERENCES "t_tiposcuenta" ("id") ON UPDATE NO ACTION ON DELETE NO ACTION,
	CONSTRAINT "1" FOREIGN KEY ("id_padre") REFERENCES "t_cuentas" ("id") ON UPDATE NO ACTION ON DELETE NO ACTION
)
;
CREATE INDEX "Índice 3" ON "t_cuentas" ("id_tipo");
CREATE INDEX "Índice 2" ON "t_cuentas" ("id_padre");


