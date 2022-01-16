CREATE TABLE IF NOT EXISTS `cons` (
  `id_evento` BIGINT NOT NULL,
  `id_plano` INT NULL,
  `faixa_etaria` VARCHAR(15) NULL,
  `sexo` VARCHAR(10) NULL,
  `cod_municipio` VARCHAR(6) NULL,
  `porte` VARCHAR(20) NULL,
  `nome_modalidade` VARCHAR(45) NULL,
  `UF` VARCHAR(2) NULL,
  `tempo_permanencia` INT NULL,
  `ano_evento` INT NULL,
  `mes_evento` INT NULL,
  `cod_carater_atendimento` INT NULL,
  `cod_tipo` INT NULL,
  `regime_internacao` INT NULL,
  `motivo_saida` INT NULL,
  `cid` VARCHAR(15) NULL,
  `diarias_uti` INT NULL,
  PRIMARY KEY (`id_evento`))
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS `det` (
  `id_evento` BIGINT NOT NULL,
  `cod_procedimento` VARCHAR(40) NULL,
  `qtd_item_informado` INT NULL,
  `valor_item_informado` DOUBLE NULL,
  `valor_item_pago_fornecedor` DOUBLE NULL,
  INDEX `fk_det_cons_idx` (`id_evento` ASC) VISIBLE,
  CONSTRAINT `fk_det_cons`
    FOREIGN KEY (`id_evento`)
    REFERENCES `cons` (`id_evento`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;
