<?xml version="1.0" encoding="UTF-8"?>
<md:node xmlns:md="http://www.stambia.com/md" defType="com.stambia.rdbms.server" id="_ACUOMKKVEe-EqZvp7at7HA" name="SIAD_PDB2" md:ref="resource.md#UUID_MD_RDBMS_ORACLE?fileId=UUID_MD_RDBMS_ORACLE$type=md$name=Oracle?" internalVersion="v2.0.0">
  <attribute defType="com.stambia.rdbms.server.module" id="_ACgbcKKVEe-EqZvp7at7HA" value="Oracle"/>
  <attribute defType="com.stambia.rdbms.server.user" id="_22yycKKXEe-EqZvp7at7HA" value="CSG2_ORA9"/>
  <attribute defType="com.stambia.rdbms.server.driver" id="_220AkKKXEe-EqZvp7at7HA" value="oracle.jdbc.OracleDriver"/>
  <attribute defType="com.stambia.rdbms.server.designerAutoCommit" id="_220AkaKXEe-EqZvp7at7HA" value="true"/>
  <attribute defType="com.stambia.rdbms.server.password" id="_220AkqKXEe-EqZvp7at7HA" value="CC91B92AF1C0218FFEDC45BF265B9571"/>
  <attribute defType="com.stambia.rdbms.server.url" id="_220Ak6KXEe-EqZvp7at7HA" value="jdbc:oracle:thin:@//195.83.93.26:1521/SIAD_PDB2"/>
  <node defType="com.stambia.rdbms.schema" id="_AHjTgKKVEe-EqZvp7at7HA" name="CSG2_ORA9">
    <attribute defType="com.stambia.rdbms.schema.name" id="_AJIA0KKVEe-EqZvp7at7HA" value="CSG2_ORA9"/>
    <attribute defType="com.stambia.rdbms.schema.rejectMask" id="_AJIn4KKVEe-EqZvp7at7HA" value="R_[targetName]"/>
    <attribute defType="com.stambia.rdbms.schema.loadMask" id="_AJKdEKKVEe-EqZvp7at7HA" value="L[number]_[targetName]"/>
    <attribute defType="com.stambia.rdbms.schema.integrationMask" id="_AJKdEaKVEe-EqZvp7at7HA" value="I_[targetName]"/>
    <node defType="com.stambia.rdbms.datastore" id="_222dnqKXEe-EqZvp7at7HA" name="ARTICLE_EXP">
      <attribute defType="com.stambia.rdbms.datastore.name" id="_222dn6KXEe-EqZvp7at7HA" value="ARTICLE_EXP"/>
      <attribute defType="com.stambia.rdbms.datastore.type" id="_222doKKXEe-EqZvp7at7HA" value="TABLE"/>
      <node defType="com.stambia.rdbms.column" id="_222doaKXEe-EqZvp7at7HA" name="COD_MRQ" position="1">
        <attribute defType="com.stambia.rdbms.column.name" id="_222doqKXEe-EqZvp7at7HA" value="COD_MRQ"/>
        <attribute defType="com.stambia.rdbms.column.nullable" id="_222do6KXEe-EqZvp7at7HA" value="1"/>
        <attribute defType="com.stambia.rdbms.column.charByte" id="_222dpKKXEe-EqZvp7at7HA" value="BYTE"/>
        <attribute defType="com.stambia.rdbms.column.type" id="_222dpaKXEe-EqZvp7at7HA" value="VARCHAR2"/>
        <attribute defType="com.stambia.rdbms.column.size" id="_222dpqKXEe-EqZvp7at7HA" value="3"/>
      </node>
      <node defType="com.stambia.rdbms.column" id="_222dp6KXEe-EqZvp7at7HA" name="LIB_MRQ" position="2">
        <attribute defType="com.stambia.rdbms.column.name" id="_222dqKKXEe-EqZvp7at7HA" value="LIB_MRQ"/>
        <attribute defType="com.stambia.rdbms.column.nullable" id="_222dqaKXEe-EqZvp7at7HA" value="1"/>
        <attribute defType="com.stambia.rdbms.column.charByte" id="_222dqqKXEe-EqZvp7at7HA" value="BYTE"/>
        <attribute defType="com.stambia.rdbms.column.type" id="_222dq6KXEe-EqZvp7at7HA" value="VARCHAR2"/>
        <attribute defType="com.stambia.rdbms.column.size" id="_222drKKXEe-EqZvp7at7HA" value="26"/>
      </node>
      <node defType="com.stambia.rdbms.column" id="_222draKXEe-EqZvp7at7HA" name="COD_ART" position="3">
        <attribute defType="com.stambia.rdbms.column.name" id="_222drqKXEe-EqZvp7at7HA" value="COD_ART"/>
        <attribute defType="com.stambia.rdbms.column.nullable" id="_222dr6KXEe-EqZvp7at7HA" value="1"/>
        <attribute defType="com.stambia.rdbms.column.charByte" id="_222dsKKXEe-EqZvp7at7HA" value="BYTE"/>
        <attribute defType="com.stambia.rdbms.column.type" id="_222dsaKXEe-EqZvp7at7HA" value="FLOAT"/>
        <attribute defType="com.stambia.rdbms.column.size" id="_222dsqKXEe-EqZvp7at7HA" value="126"/>
      </node>
      <node defType="com.stambia.rdbms.column" id="_222ds6KXEe-EqZvp7at7HA" name="LIB_PRD" position="4">
        <attribute defType="com.stambia.rdbms.column.name" id="_222dtKKXEe-EqZvp7at7HA" value="LIB_PRD"/>
        <attribute defType="com.stambia.rdbms.column.nullable" id="_222dtaKXEe-EqZvp7at7HA" value="1"/>
        <attribute defType="com.stambia.rdbms.column.charByte" id="_222dtqKXEe-EqZvp7at7HA" value="BYTE"/>
        <attribute defType="com.stambia.rdbms.column.type" id="_222dt6KXEe-EqZvp7at7HA" value="VARCHAR2"/>
        <attribute defType="com.stambia.rdbms.column.size" id="_222duKKXEe-EqZvp7at7HA" value="40"/>
      </node>
      <node defType="com.stambia.rdbms.column" id="_222duaKXEe-EqZvp7at7HA" name="LIB_COL" position="5">
        <attribute defType="com.stambia.rdbms.column.name" id="_222duqKXEe-EqZvp7at7HA" value="LIB_COL"/>
        <attribute defType="com.stambia.rdbms.column.nullable" id="_222du6KXEe-EqZvp7at7HA" value="1"/>
        <attribute defType="com.stambia.rdbms.column.charByte" id="_222dvKKXEe-EqZvp7at7HA" value="BYTE"/>
        <attribute defType="com.stambia.rdbms.column.type" id="_222dvaKXEe-EqZvp7at7HA" value="VARCHAR2"/>
        <attribute defType="com.stambia.rdbms.column.size" id="_222dvqKXEe-EqZvp7at7HA" value="21"/>
      </node>
      <node defType="com.stambia.rdbms.column" id="_222dv6KXEe-EqZvp7at7HA" name="LIB_TAI" position="6">
        <attribute defType="com.stambia.rdbms.column.name" id="_222dwKKXEe-EqZvp7at7HA" value="LIB_TAI"/>
        <attribute defType="com.stambia.rdbms.column.nullable" id="_222dwaKXEe-EqZvp7at7HA" value="1"/>
        <attribute defType="com.stambia.rdbms.column.charByte" id="_222dwqKXEe-EqZvp7at7HA" value="BYTE"/>
        <attribute defType="com.stambia.rdbms.column.type" id="_222dw6KXEe-EqZvp7at7HA" value="VARCHAR2"/>
        <attribute defType="com.stambia.rdbms.column.size" id="_222dxKKXEe-EqZvp7at7HA" value="9"/>
      </node>
      <node defType="com.stambia.rdbms.column" id="_222dxaKXEe-EqZvp7at7HA" name="FAM" position="7">
        <attribute defType="com.stambia.rdbms.column.name" id="_222dxqKXEe-EqZvp7at7HA" value="FAM"/>
        <attribute defType="com.stambia.rdbms.column.nullable" id="_222dx6KXEe-EqZvp7at7HA" value="1"/>
        <attribute defType="com.stambia.rdbms.column.charByte" id="_222dyKKXEe-EqZvp7at7HA" value="BYTE"/>
        <attribute defType="com.stambia.rdbms.column.type" id="_222dyaKXEe-EqZvp7at7HA" value="VARCHAR2"/>
        <attribute defType="com.stambia.rdbms.column.size" id="_222dyqKXEe-EqZvp7at7HA" value="25"/>
      </node>
      <node defType="com.stambia.rdbms.column" id="_222dy6KXEe-EqZvp7at7HA" name="SS_FAM" position="8">
        <attribute defType="com.stambia.rdbms.column.name" id="_222dzKKXEe-EqZvp7at7HA" value="SS_FAM"/>
        <attribute defType="com.stambia.rdbms.column.nullable" id="_222dzaKXEe-EqZvp7at7HA" value="1"/>
        <attribute defType="com.stambia.rdbms.column.charByte" id="_222dzqKXEe-EqZvp7at7HA" value="BYTE"/>
        <attribute defType="com.stambia.rdbms.column.type" id="_222dz6KXEe-EqZvp7at7HA" value="VARCHAR2"/>
        <attribute defType="com.stambia.rdbms.column.size" id="_222d0KKXEe-EqZvp7at7HA" value="30"/>
      </node>
      <node defType="com.stambia.rdbms.column" id="_222d0aKXEe-EqZvp7at7HA" name="PRX_VEN" position="9">
        <attribute defType="com.stambia.rdbms.column.name" id="_222d0qKXEe-EqZvp7at7HA" value="PRX_VEN"/>
        <attribute defType="com.stambia.rdbms.column.nullable" id="_222d06KXEe-EqZvp7at7HA" value="1"/>
        <attribute defType="com.stambia.rdbms.column.charByte" id="_222d1KKXEe-EqZvp7at7HA" value="BYTE"/>
        <attribute defType="com.stambia.rdbms.column.type" id="_222d1aKXEe-EqZvp7at7HA" value="FLOAT"/>
        <attribute defType="com.stambia.rdbms.column.size" id="_222d1qKXEe-EqZvp7at7HA" value="126"/>
      </node>
      <node defType="com.stambia.rdbms.column" id="_222d16KXEe-EqZvp7at7HA" name="LIB_GEN" position="10">
        <attribute defType="com.stambia.rdbms.column.name" id="_222d2KKXEe-EqZvp7at7HA" value="LIB_GEN"/>
        <attribute defType="com.stambia.rdbms.column.nullable" id="_222d2aKXEe-EqZvp7at7HA" value="1"/>
        <attribute defType="com.stambia.rdbms.column.charByte" id="_222d2qKXEe-EqZvp7at7HA" value="BYTE"/>
        <attribute defType="com.stambia.rdbms.column.type" id="_222d26KXEe-EqZvp7at7HA" value="VARCHAR2"/>
        <attribute defType="com.stambia.rdbms.column.size" id="_222d3KKXEe-EqZvp7at7HA" value="6"/>
      </node>
      <node defType="com.stambia.rdbms.column" id="_222d3aKXEe-EqZvp7at7HA" name="CIB_TRN_AGE" position="11">
        <attribute defType="com.stambia.rdbms.column.name" id="_222d3qKXEe-EqZvp7at7HA" value="CIB_TRN_AGE"/>
        <attribute defType="com.stambia.rdbms.column.nullable" id="_222d36KXEe-EqZvp7at7HA" value="1"/>
        <attribute defType="com.stambia.rdbms.column.charByte" id="_222d4KKXEe-EqZvp7at7HA" value="BYTE"/>
        <attribute defType="com.stambia.rdbms.column.type" id="_222d4aKXEe-EqZvp7at7HA" value="VARCHAR2"/>
        <attribute defType="com.stambia.rdbms.column.size" id="_222d4qKXEe-EqZvp7at7HA" value="11"/>
      </node>
      <node defType="com.stambia.rdbms.column" id="_222d46KXEe-EqZvp7at7HA" name="COD_CAT" position="12">
        <attribute defType="com.stambia.rdbms.column.name" id="_222d5KKXEe-EqZvp7at7HA" value="COD_CAT"/>
        <attribute defType="com.stambia.rdbms.column.nullable" id="_222d5aKXEe-EqZvp7at7HA" value="1"/>
        <attribute defType="com.stambia.rdbms.column.charByte" id="_222d5qKXEe-EqZvp7at7HA" value="BYTE"/>
        <attribute defType="com.stambia.rdbms.column.type" id="_222d56KXEe-EqZvp7at7HA" value="VARCHAR2"/>
        <attribute defType="com.stambia.rdbms.column.size" id="_222d6KKXEe-EqZvp7at7HA" value="3"/>
      </node>
      <node defType="com.stambia.rdbms.column" id="_222d6aKXEe-EqZvp7at7HA" name="LIB_CAT" position="13">
        <attribute defType="com.stambia.rdbms.column.name" id="_222d6qKXEe-EqZvp7at7HA" value="LIB_CAT"/>
        <attribute defType="com.stambia.rdbms.column.nullable" id="_222d66KXEe-EqZvp7at7HA" value="1"/>
        <attribute defType="com.stambia.rdbms.column.charByte" id="_222d7KKXEe-EqZvp7at7HA" value="BYTE"/>
        <attribute defType="com.stambia.rdbms.column.type" id="_222d7aKXEe-EqZvp7at7HA" value="VARCHAR2"/>
        <attribute defType="com.stambia.rdbms.column.size" id="_222d7qKXEe-EqZvp7at7HA" value="16"/>
      </node>
    </node>
    <node defType="com.stambia.rdbms.datastore" id="_222c1aKXEe-EqZvp7at7HA" name="TICKET_EXP">
      <attribute defType="com.stambia.rdbms.datastore.name" id="_222c1qKXEe-EqZvp7at7HA" value="TICKET_EXP"/>
      <attribute defType="com.stambia.rdbms.datastore.type" id="_222c16KXEe-EqZvp7at7HA" value="TABLE"/>
      <node defType="com.stambia.rdbms.column" id="_222c2KKXEe-EqZvp7at7HA" name="COD_ENS" position="1">
        <attribute defType="com.stambia.rdbms.column.name" id="_222c2aKXEe-EqZvp7at7HA" value="COD_ENS"/>
        <attribute defType="com.stambia.rdbms.column.nullable" id="_222c2qKXEe-EqZvp7at7HA" value="1"/>
        <attribute defType="com.stambia.rdbms.column.charByte" id="_222c26KXEe-EqZvp7at7HA" value="BYTE"/>
        <attribute defType="com.stambia.rdbms.column.type" id="_222c3KKXEe-EqZvp7at7HA" value="VARCHAR2"/>
        <attribute defType="com.stambia.rdbms.column.size" id="_222c3aKXEe-EqZvp7at7HA" value="3"/>
      </node>
      <node defType="com.stambia.rdbms.column" id="_222c3qKXEe-EqZvp7at7HA" name="LIB_ENS" position="2">
        <attribute defType="com.stambia.rdbms.column.name" id="_222c36KXEe-EqZvp7at7HA" value="LIB_ENS"/>
        <attribute defType="com.stambia.rdbms.column.nullable" id="_222c4KKXEe-EqZvp7at7HA" value="1"/>
        <attribute defType="com.stambia.rdbms.column.charByte" id="_222c4aKXEe-EqZvp7at7HA" value="BYTE"/>
        <attribute defType="com.stambia.rdbms.column.type" id="_222c4qKXEe-EqZvp7at7HA" value="VARCHAR2"/>
        <attribute defType="com.stambia.rdbms.column.size" id="_222c46KXEe-EqZvp7at7HA" value="6"/>
      </node>
      <node defType="com.stambia.rdbms.column" id="_222c5KKXEe-EqZvp7at7HA" name="LIB_MAG" position="3">
        <attribute defType="com.stambia.rdbms.column.name" id="_222c5aKXEe-EqZvp7at7HA" value="LIB_MAG"/>
        <attribute defType="com.stambia.rdbms.column.nullable" id="_222c5qKXEe-EqZvp7at7HA" value="1"/>
        <attribute defType="com.stambia.rdbms.column.charByte" id="_222c56KXEe-EqZvp7at7HA" value="BYTE"/>
        <attribute defType="com.stambia.rdbms.column.type" id="_222c6KKXEe-EqZvp7at7HA" value="VARCHAR2"/>
        <attribute defType="com.stambia.rdbms.column.size" id="_222c6aKXEe-EqZvp7at7HA" value="25"/>
      </node>
      <node defType="com.stambia.rdbms.column" id="_222c6qKXEe-EqZvp7at7HA" name="COD_ART" position="4">
        <attribute defType="com.stambia.rdbms.column.name" id="_222c66KXEe-EqZvp7at7HA" value="COD_ART"/>
        <attribute defType="com.stambia.rdbms.column.nullable" id="_222c7KKXEe-EqZvp7at7HA" value="1"/>
        <attribute defType="com.stambia.rdbms.column.charByte" id="_222c7aKXEe-EqZvp7at7HA" value="BYTE"/>
        <attribute defType="com.stambia.rdbms.column.type" id="_222c7qKXEe-EqZvp7at7HA" value="FLOAT"/>
        <attribute defType="com.stambia.rdbms.column.size" id="_222c76KXEe-EqZvp7at7HA" value="126"/>
      </node>
      <node defType="com.stambia.rdbms.column" id="_222c8KKXEe-EqZvp7at7HA" name="DAT_HEU_TIC" position="5">
        <attribute defType="com.stambia.rdbms.column.name" id="_222c8aKXEe-EqZvp7at7HA" value="DAT_HEU_TIC"/>
        <attribute defType="com.stambia.rdbms.column.nullable" id="_222c8qKXEe-EqZvp7at7HA" value="1"/>
        <attribute defType="com.stambia.rdbms.column.charByte" id="_222c86KXEe-EqZvp7at7HA" value="BYTE"/>
        <attribute defType="com.stambia.rdbms.column.type" id="_222c9KKXEe-EqZvp7at7HA" value="VARCHAR2"/>
        <attribute defType="com.stambia.rdbms.column.size" id="_222c9aKXEe-EqZvp7at7HA" value="19"/>
      </node>
      <node defType="com.stambia.rdbms.column" id="_222c9qKXEe-EqZvp7at7HA" name="NUM_TIC" position="6">
        <attribute defType="com.stambia.rdbms.column.name" id="_222c96KXEe-EqZvp7at7HA" value="NUM_TIC"/>
        <attribute defType="com.stambia.rdbms.column.nullable" id="_222c-KKXEe-EqZvp7at7HA" value="1"/>
        <attribute defType="com.stambia.rdbms.column.charByte" id="_222c-aKXEe-EqZvp7at7HA" value="BYTE"/>
        <attribute defType="com.stambia.rdbms.column.type" id="_222c-qKXEe-EqZvp7at7HA" value="FLOAT"/>
        <attribute defType="com.stambia.rdbms.column.size" id="_222c-6KXEe-EqZvp7at7HA" value="126"/>
      </node>
      <node defType="com.stambia.rdbms.column" id="_222c_KKXEe-EqZvp7at7HA" name="NUM_TIC_LIG" position="7">
        <attribute defType="com.stambia.rdbms.column.name" id="_222c_aKXEe-EqZvp7at7HA" value="NUM_TIC_LIG"/>
        <attribute defType="com.stambia.rdbms.column.nullable" id="_222c_qKXEe-EqZvp7at7HA" value="1"/>
        <attribute defType="com.stambia.rdbms.column.charByte" id="_222c_6KXEe-EqZvp7at7HA" value="BYTE"/>
        <attribute defType="com.stambia.rdbms.column.type" id="_222dAKKXEe-EqZvp7at7HA" value="FLOAT"/>
        <attribute defType="com.stambia.rdbms.column.size" id="_222dAaKXEe-EqZvp7at7HA" value="126"/>
      </node>
      <node defType="com.stambia.rdbms.column" id="_222dAqKXEe-EqZvp7at7HA" name="COD_CAI" position="8">
        <attribute defType="com.stambia.rdbms.column.name" id="_222dA6KXEe-EqZvp7at7HA" value="COD_CAI"/>
        <attribute defType="com.stambia.rdbms.column.nullable" id="_222dBKKXEe-EqZvp7at7HA" value="1"/>
        <attribute defType="com.stambia.rdbms.column.charByte" id="_222dBaKXEe-EqZvp7at7HA" value="BYTE"/>
        <attribute defType="com.stambia.rdbms.column.type" id="_222dBqKXEe-EqZvp7at7HA" value="FLOAT"/>
        <attribute defType="com.stambia.rdbms.column.size" id="_222dB6KXEe-EqZvp7at7HA" value="126"/>
      </node>
      <node defType="com.stambia.rdbms.column" id="_222dCKKXEe-EqZvp7at7HA" name="COD_VEN" position="9">
        <attribute defType="com.stambia.rdbms.column.name" id="_222dCaKXEe-EqZvp7at7HA" value="COD_VEN"/>
        <attribute defType="com.stambia.rdbms.column.nullable" id="_222dCqKXEe-EqZvp7at7HA" value="1"/>
        <attribute defType="com.stambia.rdbms.column.charByte" id="_222dC6KXEe-EqZvp7at7HA" value="BYTE"/>
        <attribute defType="com.stambia.rdbms.column.type" id="_222dDKKXEe-EqZvp7at7HA" value="VARCHAR2"/>
        <attribute defType="com.stambia.rdbms.column.size" id="_222dDaKXEe-EqZvp7at7HA" value="6"/>
      </node>
      <node defType="com.stambia.rdbms.column" id="_222dDqKXEe-EqZvp7at7HA" name="QTE" position="10">
        <attribute defType="com.stambia.rdbms.column.name" id="_222dD6KXEe-EqZvp7at7HA" value="QTE"/>
        <attribute defType="com.stambia.rdbms.column.nullable" id="_222dEKKXEe-EqZvp7at7HA" value="1"/>
        <attribute defType="com.stambia.rdbms.column.charByte" id="_222dEaKXEe-EqZvp7at7HA" value="BYTE"/>
        <attribute defType="com.stambia.rdbms.column.type" id="_222dEqKXEe-EqZvp7at7HA" value="FLOAT"/>
        <attribute defType="com.stambia.rdbms.column.size" id="_222dE6KXEe-EqZvp7at7HA" value="126"/>
      </node>
      <node defType="com.stambia.rdbms.column" id="_222dFKKXEe-EqZvp7at7HA" name="MNT_BRU" position="11">
        <attribute defType="com.stambia.rdbms.column.name" id="_222dFaKXEe-EqZvp7at7HA" value="MNT_BRU"/>
        <attribute defType="com.stambia.rdbms.column.nullable" id="_222dFqKXEe-EqZvp7at7HA" value="1"/>
        <attribute defType="com.stambia.rdbms.column.charByte" id="_222dF6KXEe-EqZvp7at7HA" value="BYTE"/>
        <attribute defType="com.stambia.rdbms.column.type" id="_222dGKKXEe-EqZvp7at7HA" value="FLOAT"/>
        <attribute defType="com.stambia.rdbms.column.size" id="_222dGaKXEe-EqZvp7at7HA" value="126"/>
      </node>
      <node defType="com.stambia.rdbms.column" id="_222dGqKXEe-EqZvp7at7HA" name="MNT_TTC" position="12">
        <attribute defType="com.stambia.rdbms.column.name" id="_222dG6KXEe-EqZvp7at7HA" value="MNT_TTC"/>
        <attribute defType="com.stambia.rdbms.column.nullable" id="_222dHKKXEe-EqZvp7at7HA" value="1"/>
        <attribute defType="com.stambia.rdbms.column.charByte" id="_222dHaKXEe-EqZvp7at7HA" value="BYTE"/>
        <attribute defType="com.stambia.rdbms.column.type" id="_222dHqKXEe-EqZvp7at7HA" value="FLOAT"/>
        <attribute defType="com.stambia.rdbms.column.size" id="_222dH6KXEe-EqZvp7at7HA" value="126"/>
      </node>
      <node defType="com.stambia.rdbms.column" id="_222dIKKXEe-EqZvp7at7HA" name="COD_DEV" position="13">
        <attribute defType="com.stambia.rdbms.column.name" id="_222dIaKXEe-EqZvp7at7HA" value="COD_DEV"/>
        <attribute defType="com.stambia.rdbms.column.nullable" id="_222dIqKXEe-EqZvp7at7HA" value="1"/>
        <attribute defType="com.stambia.rdbms.column.charByte" id="_222dI6KXEe-EqZvp7at7HA" value="BYTE"/>
        <attribute defType="com.stambia.rdbms.column.type" id="_222dJKKXEe-EqZvp7at7HA" value="VARCHAR2"/>
        <attribute defType="com.stambia.rdbms.column.size" id="_222dJaKXEe-EqZvp7at7HA" value="3"/>
      </node>
      <node defType="com.stambia.rdbms.column" id="_222dJqKXEe-EqZvp7at7HA" name="TX_TVA" position="14">
        <attribute defType="com.stambia.rdbms.column.name" id="_222dJ6KXEe-EqZvp7at7HA" value="TX_TVA"/>
        <attribute defType="com.stambia.rdbms.column.nullable" id="_222dKKKXEe-EqZvp7at7HA" value="1"/>
        <attribute defType="com.stambia.rdbms.column.charByte" id="_222dKaKXEe-EqZvp7at7HA" value="BYTE"/>
        <attribute defType="com.stambia.rdbms.column.type" id="_222dKqKXEe-EqZvp7at7HA" value="FLOAT"/>
        <attribute defType="com.stambia.rdbms.column.size" id="_222dK6KXEe-EqZvp7at7HA" value="126"/>
      </node>
      <node defType="com.stambia.rdbms.column" id="_222dLKKXEe-EqZvp7at7HA" name="REM_LIN" position="15">
        <attribute defType="com.stambia.rdbms.column.name" id="_222dLaKXEe-EqZvp7at7HA" value="REM_LIN"/>
        <attribute defType="com.stambia.rdbms.column.nullable" id="_222dLqKXEe-EqZvp7at7HA" value="1"/>
        <attribute defType="com.stambia.rdbms.column.charByte" id="_222dL6KXEe-EqZvp7at7HA" value="BYTE"/>
        <attribute defType="com.stambia.rdbms.column.type" id="_222dMKKXEe-EqZvp7at7HA" value="FLOAT"/>
        <attribute defType="com.stambia.rdbms.column.size" id="_222dMaKXEe-EqZvp7at7HA" value="126"/>
      </node>
      <node defType="com.stambia.rdbms.column" id="_222dMqKXEe-EqZvp7at7HA" name="REM_TIC" position="16">
        <attribute defType="com.stambia.rdbms.column.name" id="_222dM6KXEe-EqZvp7at7HA" value="REM_TIC"/>
        <attribute defType="com.stambia.rdbms.column.nullable" id="_222dNKKXEe-EqZvp7at7HA" value="1"/>
        <attribute defType="com.stambia.rdbms.column.charByte" id="_222dNaKXEe-EqZvp7at7HA" value="BYTE"/>
        <attribute defType="com.stambia.rdbms.column.type" id="_222dNqKXEe-EqZvp7at7HA" value="FLOAT"/>
        <attribute defType="com.stambia.rdbms.column.size" id="_222dN6KXEe-EqZvp7at7HA" value="126"/>
      </node>
      <node defType="com.stambia.rdbms.column" id="_222dOKKXEe-EqZvp7at7HA" name="TX_DEV" position="17">
        <attribute defType="com.stambia.rdbms.column.name" id="_222dOaKXEe-EqZvp7at7HA" value="TX_DEV"/>
        <attribute defType="com.stambia.rdbms.column.nullable" id="_222dOqKXEe-EqZvp7at7HA" value="1"/>
        <attribute defType="com.stambia.rdbms.column.charByte" id="_222dO6KXEe-EqZvp7at7HA" value="BYTE"/>
        <attribute defType="com.stambia.rdbms.column.type" id="_222dPKKXEe-EqZvp7at7HA" value="FLOAT"/>
        <attribute defType="com.stambia.rdbms.column.size" id="_222dPaKXEe-EqZvp7at7HA" value="126"/>
      </node>
      <node defType="com.stambia.rdbms.column" id="_222dPqKXEe-EqZvp7at7HA" name="COD_PAY" position="18">
        <attribute defType="com.stambia.rdbms.column.name" id="_222dP6KXEe-EqZvp7at7HA" value="COD_PAY"/>
        <attribute defType="com.stambia.rdbms.column.nullable" id="_222dQKKXEe-EqZvp7at7HA" value="1"/>
        <attribute defType="com.stambia.rdbms.column.charByte" id="_222dQaKXEe-EqZvp7at7HA" value="BYTE"/>
        <attribute defType="com.stambia.rdbms.column.type" id="_222dQqKXEe-EqZvp7at7HA" value="VARCHAR2"/>
        <attribute defType="com.stambia.rdbms.column.size" id="_222dQ6KXEe-EqZvp7at7HA" value="2"/>
      </node>
      <node defType="com.stambia.rdbms.column" id="_222dRKKXEe-EqZvp7at7HA" name="LIB_PAY" position="19">
        <attribute defType="com.stambia.rdbms.column.name" id="_222dRaKXEe-EqZvp7at7HA" value="LIB_PAY"/>
        <attribute defType="com.stambia.rdbms.column.nullable" id="_222dRqKXEe-EqZvp7at7HA" value="1"/>
        <attribute defType="com.stambia.rdbms.column.charByte" id="_222dR6KXEe-EqZvp7at7HA" value="BYTE"/>
        <attribute defType="com.stambia.rdbms.column.type" id="_222dSKKXEe-EqZvp7at7HA" value="VARCHAR2"/>
        <attribute defType="com.stambia.rdbms.column.size" id="_222dSaKXEe-EqZvp7at7HA" value="8"/>
      </node>
      <node defType="com.stambia.rdbms.column" id="_222dSqKXEe-EqZvp7at7HA" name="ADR1" position="20">
        <attribute defType="com.stambia.rdbms.column.name" id="_222dS6KXEe-EqZvp7at7HA" value="ADR1"/>
        <attribute defType="com.stambia.rdbms.column.nullable" id="_222dTKKXEe-EqZvp7at7HA" value="1"/>
        <attribute defType="com.stambia.rdbms.column.charByte" id="_222dTaKXEe-EqZvp7at7HA" value="BYTE"/>
        <attribute defType="com.stambia.rdbms.column.type" id="_222dTqKXEe-EqZvp7at7HA" value="VARCHAR2"/>
        <attribute defType="com.stambia.rdbms.column.size" id="_222dT6KXEe-EqZvp7at7HA" value="43"/>
      </node>
      <node defType="com.stambia.rdbms.column" id="_222dUKKXEe-EqZvp7at7HA" name="ADR2" position="21">
        <attribute defType="com.stambia.rdbms.column.name" id="_222dUaKXEe-EqZvp7at7HA" value="ADR2"/>
        <attribute defType="com.stambia.rdbms.column.nullable" id="_222dUqKXEe-EqZvp7at7HA" value="1"/>
        <attribute defType="com.stambia.rdbms.column.charByte" id="_222dU6KXEe-EqZvp7at7HA" value="BYTE"/>
        <attribute defType="com.stambia.rdbms.column.type" id="_222dVKKXEe-EqZvp7at7HA" value="VARCHAR2"/>
        <attribute defType="com.stambia.rdbms.column.size" id="_222dVaKXEe-EqZvp7at7HA" value="33"/>
      </node>
      <node defType="com.stambia.rdbms.column" id="_222dVqKXEe-EqZvp7at7HA" name="ADR3" position="22">
        <attribute defType="com.stambia.rdbms.column.name" id="_222dV6KXEe-EqZvp7at7HA" value="ADR3"/>
        <attribute defType="com.stambia.rdbms.column.nullable" id="_222dWKKXEe-EqZvp7at7HA" value="1"/>
        <attribute defType="com.stambia.rdbms.column.charByte" id="_222dWaKXEe-EqZvp7at7HA" value="BYTE"/>
        <attribute defType="com.stambia.rdbms.column.type" id="_222dWqKXEe-EqZvp7at7HA" value="VARCHAR2"/>
        <attribute defType="com.stambia.rdbms.column.size" id="_222dW6KXEe-EqZvp7at7HA" value="52"/>
      </node>
      <node defType="com.stambia.rdbms.column" id="_222dXKKXEe-EqZvp7at7HA" name="VIL_MAG" position="23">
        <attribute defType="com.stambia.rdbms.column.name" id="_222dXaKXEe-EqZvp7at7HA" value="VIL_MAG"/>
        <attribute defType="com.stambia.rdbms.column.nullable" id="_222dXqKXEe-EqZvp7at7HA" value="1"/>
        <attribute defType="com.stambia.rdbms.column.charByte" id="_222dX6KXEe-EqZvp7at7HA" value="BYTE"/>
        <attribute defType="com.stambia.rdbms.column.type" id="_222dYKKXEe-EqZvp7at7HA" value="VARCHAR2"/>
        <attribute defType="com.stambia.rdbms.column.size" id="_222dYaKXEe-EqZvp7at7HA" value="22"/>
      </node>
      <node defType="com.stambia.rdbms.column" id="_222dYqKXEe-EqZvp7at7HA" name="COD_POS" position="24">
        <attribute defType="com.stambia.rdbms.column.name" id="_222dY6KXEe-EqZvp7at7HA" value="COD_POS"/>
        <attribute defType="com.stambia.rdbms.column.nullable" id="_222dZKKXEe-EqZvp7at7HA" value="1"/>
        <attribute defType="com.stambia.rdbms.column.charByte" id="_222dZaKXEe-EqZvp7at7HA" value="BYTE"/>
        <attribute defType="com.stambia.rdbms.column.type" id="_222dZqKXEe-EqZvp7at7HA" value="FLOAT"/>
        <attribute defType="com.stambia.rdbms.column.size" id="_222dZ6KXEe-EqZvp7at7HA" value="126"/>
      </node>
      <node defType="com.stambia.rdbms.column" id="_222daKKXEe-EqZvp7at7HA" name="DEP_MAG" position="25">
        <attribute defType="com.stambia.rdbms.column.name" id="_222daaKXEe-EqZvp7at7HA" value="DEP_MAG"/>
        <attribute defType="com.stambia.rdbms.column.nullable" id="_222daqKXEe-EqZvp7at7HA" value="1"/>
        <attribute defType="com.stambia.rdbms.column.charByte" id="_222da6KXEe-EqZvp7at7HA" value="BYTE"/>
        <attribute defType="com.stambia.rdbms.column.type" id="_222dbKKXEe-EqZvp7at7HA" value="VARCHAR2"/>
        <attribute defType="com.stambia.rdbms.column.size" id="_222dbaKXEe-EqZvp7at7HA" value="20"/>
      </node>
      <node defType="com.stambia.rdbms.column" id="_222dbqKXEe-EqZvp7at7HA" name="REG_MAG" position="26">
        <attribute defType="com.stambia.rdbms.column.name" id="_222db6KXEe-EqZvp7at7HA" value="REG_MAG"/>
        <attribute defType="com.stambia.rdbms.column.nullable" id="_222dcKKXEe-EqZvp7at7HA" value="1"/>
        <attribute defType="com.stambia.rdbms.column.charByte" id="_222dcaKXEe-EqZvp7at7HA" value="BYTE"/>
        <attribute defType="com.stambia.rdbms.column.type" id="_222dcqKXEe-EqZvp7at7HA" value="VARCHAR2"/>
        <attribute defType="com.stambia.rdbms.column.size" id="_222dc6KXEe-EqZvp7at7HA" value="26"/>
      </node>
      <node defType="com.stambia.rdbms.column" id="_222ddKKXEe-EqZvp7at7HA" name="TEL" position="27">
        <attribute defType="com.stambia.rdbms.column.name" id="_222ddaKXEe-EqZvp7at7HA" value="TEL"/>
        <attribute defType="com.stambia.rdbms.column.nullable" id="_222ddqKXEe-EqZvp7at7HA" value="1"/>
        <attribute defType="com.stambia.rdbms.column.charByte" id="_222dd6KXEe-EqZvp7at7HA" value="BYTE"/>
        <attribute defType="com.stambia.rdbms.column.type" id="_222deKKXEe-EqZvp7at7HA" value="VARCHAR2"/>
        <attribute defType="com.stambia.rdbms.column.size" id="_222deaKXEe-EqZvp7at7HA" value="17"/>
      </node>
      <node defType="com.stambia.rdbms.column" id="_222deqKXEe-EqZvp7at7HA" name="EMAIL" position="28">
        <attribute defType="com.stambia.rdbms.column.name" id="_222de6KXEe-EqZvp7at7HA" value="EMAIL"/>
        <attribute defType="com.stambia.rdbms.column.nullable" id="_222dfKKXEe-EqZvp7at7HA" value="1"/>
        <attribute defType="com.stambia.rdbms.column.charByte" id="_222dfaKXEe-EqZvp7at7HA" value="BYTE"/>
        <attribute defType="com.stambia.rdbms.column.type" id="_222dfqKXEe-EqZvp7at7HA" value="VARCHAR2"/>
        <attribute defType="com.stambia.rdbms.column.size" id="_222df6KXEe-EqZvp7at7HA" value="31"/>
      </node>
      <node defType="com.stambia.rdbms.column" id="_222dgKKXEe-EqZvp7at7HA" name="LNG" position="29">
        <attribute defType="com.stambia.rdbms.column.name" id="_222dgaKXEe-EqZvp7at7HA" value="LNG"/>
        <attribute defType="com.stambia.rdbms.column.nullable" id="_222dgqKXEe-EqZvp7at7HA" value="1"/>
        <attribute defType="com.stambia.rdbms.column.charByte" id="_222dg6KXEe-EqZvp7at7HA" value="BYTE"/>
        <attribute defType="com.stambia.rdbms.column.type" id="_222dhKKXEe-EqZvp7at7HA" value="FLOAT"/>
        <attribute defType="com.stambia.rdbms.column.size" id="_222dhaKXEe-EqZvp7at7HA" value="126"/>
      </node>
      <node defType="com.stambia.rdbms.column" id="_222dhqKXEe-EqZvp7at7HA" name="LAT" position="30">
        <attribute defType="com.stambia.rdbms.column.name" id="_222dh6KXEe-EqZvp7at7HA" value="LAT"/>
        <attribute defType="com.stambia.rdbms.column.nullable" id="_222diKKXEe-EqZvp7at7HA" value="1"/>
        <attribute defType="com.stambia.rdbms.column.charByte" id="_222diaKXEe-EqZvp7at7HA" value="BYTE"/>
        <attribute defType="com.stambia.rdbms.column.type" id="_222diqKXEe-EqZvp7at7HA" value="FLOAT"/>
        <attribute defType="com.stambia.rdbms.column.size" id="_222di6KXEe-EqZvp7at7HA" value="126"/>
      </node>
      <node defType="com.stambia.rdbms.column" id="_222djKKXEe-EqZvp7at7HA" name="DAT_OUV" position="31">
        <attribute defType="com.stambia.rdbms.column.name" id="_222djaKXEe-EqZvp7at7HA" value="DAT_OUV"/>
        <attribute defType="com.stambia.rdbms.column.nullable" id="_222djqKXEe-EqZvp7at7HA" value="1"/>
        <attribute defType="com.stambia.rdbms.column.charByte" id="_222dj6KXEe-EqZvp7at7HA" value="BYTE"/>
        <attribute defType="com.stambia.rdbms.column.type" id="_222dkKKXEe-EqZvp7at7HA" value="VARCHAR2"/>
        <attribute defType="com.stambia.rdbms.column.size" id="_222dkaKXEe-EqZvp7at7HA" value="10"/>
      </node>
      <node defType="com.stambia.rdbms.column" id="_222dkqKXEe-EqZvp7at7HA" name="DAT_FRM" position="32">
        <attribute defType="com.stambia.rdbms.column.name" id="_222dk6KXEe-EqZvp7at7HA" value="DAT_FRM"/>
        <attribute defType="com.stambia.rdbms.column.nullable" id="_222dlKKXEe-EqZvp7at7HA" value="1"/>
        <attribute defType="com.stambia.rdbms.column.charByte" id="_222dlaKXEe-EqZvp7at7HA" value="BYTE"/>
        <attribute defType="com.stambia.rdbms.column.type" id="_222dlqKXEe-EqZvp7at7HA" value="FLOAT"/>
        <attribute defType="com.stambia.rdbms.column.size" id="_222dl6KXEe-EqZvp7at7HA" value="126"/>
      </node>
      <node defType="com.stambia.rdbms.column" id="_222dmKKXEe-EqZvp7at7HA" name="SCHEDULE" position="33">
        <attribute defType="com.stambia.rdbms.column.name" id="_222dmaKXEe-EqZvp7at7HA" value="SCHEDULE"/>
        <attribute defType="com.stambia.rdbms.column.nullable" id="_222dmqKXEe-EqZvp7at7HA" value="1"/>
        <attribute defType="com.stambia.rdbms.column.charByte" id="_222dm6KXEe-EqZvp7at7HA" value="BYTE"/>
        <attribute defType="com.stambia.rdbms.column.type" id="_222dnKKXEe-EqZvp7at7HA" value="VARCHAR2"/>
        <attribute defType="com.stambia.rdbms.column.size" id="_222dnaKXEe-EqZvp7at7HA" value="174"/>
      </node>
    </node>
  </node>
</md:node>